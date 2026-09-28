url = "https://salsa.debian.org/cloud-team/cloud-initramfs-tools/-/tags"
pattern = r"debian/([0-9.]+.debian[0-9]+)<"


def fetch_versions(self, src):
    return map(lambda v: v.replace(".debian", "_p"), self.fetch_versions(src))
