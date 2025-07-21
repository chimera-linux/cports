pkgname = "maven"
pkgver = "3.9.11"
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
    "f312bb9db25937f1fd7ca1d53a086a3cdde596086147a42a75af027058810b9e",
    "4b7195b6a4f5c81af4c0212677a32ee8143643401bc6e1e8412e6b06ea82beac",
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
