import pyrealsense2 as rs
import numpy as np

class RealSenseCamera:

    def __init__(self, image_width=640, image_height=480):
        self.image_width = image_width
        self.image_height = image_height
        self.pipeline = None
        self.intrinsics = None
        self.depth_scale = None
        self.align = None

        self.color_image = None
        self.depth_image = None
        
    def connect(self):
        self.pipeline = rs.pipeline()
        config = rs.config()

        config.enable_stream(rs.stream.depth, self.image_width, self.image_height, rs.format.z16, 30)
        config.enable_stream(rs.stream.color, self.image_width, self.image_height, rs.format.bgr8, 30)

        profile = self.pipeline.start(config)
        rgb_profile = profile.get_stream(rs.stream.color)
        self.intrinsics = rgb_profile.as_video_stream_profile().get_intrinsics()
        self.depth_scale = profile.get_device().first_depth_sensor().get_depth_scale()
        self.align = rs.align(rs.stream.color)
    
    def disconnect(self):
        self.pipeline.stop()

    def acquire_frame(self):
        frames = self.pipeline.wait_for_frames()
        aligned_frames = self.align.process(frames)
        color_frame = aligned_frames.get_color_frame()
        depth_frame = aligned_frames.get_depth_frame()
        if not color_frame or not depth_frame:
            return False
        
        self.color_image = np.asanyarray(color_frame.get_data())
        self.depth_image = np.expand_dims(np.asanyarray(depth_frame.get_data()), axis=2)
        return True
    
    def deproject_pixel_to_point(self, cx, cy, depth):
        return rs.rs2_deproject_pixel_to_point(self.intrinsics, [cx, cy], depth)
    
    def get_depth(self, cx, cy, apply_kernel=False, kernel_size=9, n_classes=10):
        if apply_kernel:
            half_kernel = kernel_size//2
            kernel = self.depth_image[max(0, cy - half_kernel):min(self.image_height, cy + half_kernel + 1),
                                      max(0, cx - half_kernel):min(self.image_width, cx + half_kernel + 1)]
            kernel_values = [value for value in kernel.flatten() if value > 0]
            if kernel_values.size > 0:
                return np.mean(kernel_values)
            else:
                return 0

            """ kernel_values = np.sort(kernel_values)
            if kernel_values.size == 0:
                return 0
            
            modal_classes = [[] for _ in range(n_classes)]
            start_value = min(kernel_values)
            end_value = max(kernel_values)
            class_range = (end_value - start_value)/n_classes
            for modal_class_index in range(n_classes):
                for value in kernel_values:
                    if (start_value + modal_class_index*class_range) <= value < (start_value + (modal_class_index + 1)*class_range):
                        modal_classes[modal_class_index].append(value)
                    elif modal_class_index == (n_classes - 1) and value == end_value:
                        modal_classes[modal_class_index].append(value)
            cardinalities = [len(modal_class) for modal_class in modal_classes]
            depth = modal_classes[np.argmax(cardinalities)][0]
            return depth """
        else:
            if 0 <= cx < self.image_width and 0 <= cy < self.image_height:
                return self.depth_image[cy, cx].item()
            else:
                return 0
    