import re
import shlex


def strip_attach(pkg, strip_list, no_split=[]):
    do_split = pkg.rparent.options["debug"] and pkg.rparent.build_dbg
    noset = {str(arg) for arg in no_split}

    # prepare a makefile, oh no
    with open(pkg.destdir / "Makefile", "w") as mkf:
        mkl = sorted([str(arg) for arg in strip_list])
        rll = []
        rec = re.compile(r"[\s/.]")
        for mkp in mkl:
            mkr = rec.sub("_", mkp)
            cmdl = []
            if pkg.rparent.stage > 0:
                cmdl.append("strip-split")
                if do_split and mkp not in noset:
                    cmdl.append("-d")
                cmdl += [str(pkg.chroot_destdir), mkp]
            else:
                # just a very basic strip for stage0 bootstrap
                cmdl = [
                    "/usr/bin/" + pkg.rparent.get_tool("STRIP"),
                    "--strip-debug",
                    str(pkg.chroot_destdir / mkp),
                ]
            mkf.write(f"{mkr}:\n\t{shlex.join(cmdl)}\n\n")
            rll.append(mkr)
        mks = " ".join(rll)
        mkf.write(f".PHONY: {mks}\nall: {mks}\n")

    # invoke
    pkg.rparent.do(
        "make",
        "--silent",
        "--no-print-directory",
        f"-j{pkg.rparent.conf_jobs}",
        "-C",
        str(pkg.chroot_destdir),
        "all",
    )

    # remove the leftover makefile
    (pkg.destdir / "Makefile").unlink()
