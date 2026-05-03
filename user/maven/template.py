pkgname = "maven"
pkgver = "3.9.15"
pkgrel = 0
hostmakedepends = ["openjdk25"]
depends = ["virtual:java-jre!openjdk25-jre"]
pkgdesc = "Software project management and comprehension tool"
license = "Apache-2.0"
url = "https://maven.apache.org"
source = [
    f"https://dlcdn.apache.org/maven/maven-3/{pkgver}/source/apache-maven-{pkgver}-src.tar.gz",
    f"https://dlcdn.apache.org/maven/maven-3/{pkgver}/binaries/apache-maven-{pkgver}-bin.tar.gz",
]
source_paths = [
    ".",
    "bootstrap",
]
sha256 = [
    "1a6dcd849a3eefdd975ca0ce8f00f2778b892136352680e78573a0a1280728da",
    "36182f85e91128cd5c4608462ac92194e7a30638f65034de66f4e1b00600a6fc",
]


def prepare(self):
    self.do(
        "./bootstrap/bin/mvn",
        "org.apache.maven.plugins:maven-dependency-plugin:2.8:go-offline",
        "-Dmaven.repo.local=/cbuild_cache/maven",
        allow_network=True,
    )
    # Workaround upstream issue with fetching dependencies
    self.do(
        "./bootstrap/bin/mvn",
        "verify",
        "--fail-never",
        "-Dmaven.repo.local=/cbuild_cache/maven",
        allow_network=True,
    )


def build(self):
    self.do(
        "./bootstrap/bin/mvn",
        "-o",
        "package",
        "-DskipTests",
        "-Drat.skip=true",
        "-Dmaven.repo.local=/cbuild_cache/maven",
        "-DdistributionTargetDir=out",
    )


def check(self):
    self.do(
        "./bootstrap/bin/mvn",
        "-o",
        "test",
        "-Drat.skip=true",
        "-Dmaven.repo.local=/cbuild_cache/maven",
    )


def install(self):
    self.install_files("apache-maven/out", "usr/lib/", name="maven")

    self.install_dir("usr/bin")
    for bin in ["mvn", "mvnDebug", "mvnyjp"]:
        self.install_link(
            f"usr/bin/{bin}",
            f"../lib/maven/bin/{bin}",
        )
