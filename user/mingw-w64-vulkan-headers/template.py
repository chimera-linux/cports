pkgname = "mingw-w64-vulkan-headers"
pkgver = "0.0"
pkgrel = 0
build_style = "meta"
depends = []
pkgdesc = "Metapackage for Windows development"
license = "custom:meta"
url = "https://www.khronos.org/vulkan"

_targets = ["x86_64", "i686", "armv7", "aarch64"]


def _gen(an):
    at = an + "-w64-mingw32"

    @subpackage(f"mingw-w64-vulkan-headers-{an}")
    def _(self):
        self.subdesc = f"{an} support"
        self.depends = ["vulkan-headers"]
        self.options = ["brokenlinks"]

        def install():
            # these are all the directories that are installed by vulkan-headers package
            _dirs = [
                "include/vulkan",
                "include/vk_video",
                "share/cmake/VulkanHeaders",
                "share/vulkan/registry",
            ]
            for d in _dirs:
                dstp = f"usr/{at}/{d}"
                # One "../" per path segment in d  (== 1 + number of slashes)
                depth = d.count("/") + 1  # or: len(d.split("/"))
                _tgt = "../" * depth + d
                self.make_link(dstp, _tgt)

        return install

    depends.append(self.with_pkgver(f"mingw-w64-vulkan-headers-{an}"))


for _an in _targets:
    _gen(_an)
