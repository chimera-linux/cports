pkgname = "maven"
pkgver = "3.9.10"
pkgrel = 0
hostmakedepends = ["openjdk21"]
depends = ["virtual:java-jre!openjdk21-jre"]
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
    "6617e95a1907e7e560ea7cb8e31e3d0c074a13165ba737458b150f22fd8c2c2a",
    "e036059b0ac63cdcc934afffaa125c9bf3f4a4cd2d2b9995e1aee92190a0979c",
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
