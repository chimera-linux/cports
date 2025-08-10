pattern = r"R-([0-9.]+)"


def collect_sources(self):
    # look for both current major version and next major version
    major = int(self.pkgver.split(".")[0])
    return [
        f"https://cran.r-project.org/src/base/R-{major}/",
        f"https://cran.r-project.org/src/base/R-{major + 1}/",
    ]
