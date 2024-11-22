import os
import re
import tempfile


def invoke(pkg):
    default_shebang = b"#!/usr/bin/python3"

    for v in pkg.destdir.rglob("*"):
        # skip those early
        if v.is_symlink() or not v.is_file():
            continue
        # read files in binary so that we don't accidentally try decoding
        # stuff like executables and libraries as unicode, which would fail
        with open(v, "rb") as fhandle:
            # eliminate things which definitely do not have a shebang
            if fhandle.read(2) != b"#!":
                continue
            # match the shebang more specifically against a pattern
            rm = re.match(
                rb"^.*(\s|/)(python([0-9](\.[0-9]+)?)?)(\s+.*|$)",
                fhandle.readline(),
            )
            # no match, skip
            if not rm:
                continue
            majver = rm[3]
            # unversioned, major-versioned or full-versioned
            if not majver:
                shebang = default_shebang
            else:
                fidx = majver.find(b".")
                if fidx > 0:
                    majver = majver[:fidx]
                shebang = b"#!/usr/bin/python" + majver
            # convert
            bfile = v.relative_to(pkg.destdir)
            with tempfile.NamedTemporaryFile(dir=v.parent) as nf:
                mode = v.stat().st_mode
                # write new shebang
                nf.write(shebang)
                nf.write(b"\n")
                # write rest of original file
                while True:
                    ln = fhandle.readline()
                    if len(ln) == 0:
                        break
                    nf.write(ln)
                # remove old file
                v.unlink()
                # rename new file to old
                os.link(nf.name, v)
                # set mode to whatever it was
                v.chmod(mode)
            # we're done
            print(f"  Shebang converted to '{shebang.decode()}': {bfile}")
