def install(pkg):
    zig_pkg_hash = (
        pkg.do(
            "zig",
            "fetch",
            "--global-cache-dir",
            ".zig-cache",
            ".",
            capture_output=True,
        )
        .stdout.strip()
        .decode("utf-8")
    )
    
    pkg.install_files(
        ".zig-cache/p/" + zig_pkg_hash,
        "usr/src/zig/packages/",
    )
