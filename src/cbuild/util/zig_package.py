def install(pkg):
    zig_pkg_hash = (
        pkg.do(
            "zig",
            "fetch",
            "--global-cache-dir",
            "/tmp",
            ".",
            capture_output=True,
        )
        .stdout.strip()
        .decode("utf-8")
    )

    pkg.install_files(
        "/tmp/p/" + zig_pkg_hash,
        "usr/src/zig/packages/",
    )
