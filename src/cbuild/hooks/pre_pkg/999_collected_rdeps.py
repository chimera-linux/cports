def invoke(pkg):
    if not (pkg.destdir / "rdeps").is_file():
        return

    pkg.logger.out_plain("   " + (pkg.destdir / "rdeps").read_text())
