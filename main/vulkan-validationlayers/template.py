pkgname = "vulkan-validationlayers"
pkgver = "1.3.302"
pkgrel = 1
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
    "-DBUILD_WERROR=OFF",
    "-DUSE_ROBIN_HOOD_HASHING=ON",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "libx11-devel",
    "libxcb-devel",
    "libxrandr-devel",
    "spirv-tools-devel",
    "vulkan-headers",
    "vulkan-utility-libraries",
    "wayland-devel",
]
pkgdesc = "Validation layers to catch Vulkan issues"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Apache-2.0"
url = "https://vulkan.lunarg.com/doc/sdk/latest/linux/khronos_validation_layer.html"
source = [
    f"https://github.com/KhronosGroup/Vulkan-ValidationLayers/archive/refs/tags/v{pkgver}.tar.gz",
    "https://github.com/KhronosGroup/SPIRV-Headers/archive/cb6b2c32dbfc3257c1e9142a116fe9ee3d9b80a2.tar.gz",
    "https://github.com/martinus/robin-hood-hashing/archive/7697343363af4cc3f42cab17be49e6af9ab181e2.tar.gz",
]
source_paths = [
    ".",
    "spirv-headers",
    "layers/robinhood",
]
sha256 = [
    "78c49ebbe65c1034190d5d9ec57adea47833675d7f8b3b41fff86291a1e8fead",
    "2bfe8f3006d5b5e350cdc32bcee54f894d65d8a2932574f399e7cd0b3d787044",
    "bce88bee05812abd863e8ae045757b66116fc9d7e880e649916d8eb71a10fa9f",
]
# lol; drop on next release
tool_flags = {
    "CXXFLAGS": [
        "-Dsafe_VkBindDescriptorSetsInfoKHR=safe_VkBindDescriptorSetsInfo",
        "-Dsafe_VkCopyImageToImageInfoEXT=safe_VkCopyImageToImageInfo",
        "-Dsafe_VkCopyImageToMemoryInfoEXT=safe_VkCopyImageToMemoryInfo",
        "-Dsafe_VkCopyMemoryToImageInfoEXT=safe_VkCopyMemoryToImageInfo",
        "-Dsafe_VkHostImageLayoutTransitionInfoEXT=safe_VkHostImageLayoutTransitionInfo",
        "-Dsafe_VkMemoryMapInfoKHR=safe_VkMemoryMapInfo",
        "-Dsafe_VkMemoryUnmapInfoKHR=safe_VkMemoryUnmapInfo",
        "-Dsafe_VkPushConstantsInfoKHR=safe_VkPushConstantsInfo",
        "-Dsafe_VkPushDescriptorSetInfoKHR=safe_VkPushDescriptorSetInfo",
        "-Dstring_VkBufferUsageFlags2KHR=string_VkBufferUsageFlags2",
        "-Dstring_VkHostImageCopyFlagsEXT=string_VkHostImageCopyFlags",
        "-Dstring_VkLineRasterizationModeKHR=string_VkLineRasterizationMode",
        "-Dstring_VkMemoryUnmapFlagsKHR=string_VkMemoryUnmapFlags",
        "-Dstring_VkPipelineCreateFlags2KHR=string_VkPipelineCreateFlags2",
        "-Dstring_VkPipelineCreateFlagBits2KHR=string_VkPipelineCreateFlagBits2",
        "-Dstring_VkPipelineRobustnessBufferBehaviorEXT=string_VkPipelineRobustnessBufferBehavior",
        "-Dstring_VkPipelineRobustnessImageBehaviorEXT=string_VkPipelineRobustnessImageBehavior",
        "-Dstring_VkQueueGlobalPriorityKHR=string_VkQueueGlobalPriority",
    ]
}
