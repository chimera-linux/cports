url = "https://codeberg.org/IPMITool/ipmitool/tags"
pattern = r"IPMITOOL_([\d\_]+).tar.gz"


def fetch_versions(self, src):
    return map(lambda v: v.replace("_", "."), self.fetch_versions(src))
