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
                # check for python zipapps; they have the shebang followed
                # by line feed followed by a standard zip archive
                ln = fhandle.readline()
                if ln.startswith(b"\x50\x4b\x03\x04"):
                    pkg.error(
                        f"found Python zipapp: {bfile}",
                        hint="change the template to package plain Python sources",
                    )
                # write the rest of the script
                while len(ln) > 0:
                    nf.write(ln)
                    ln = fhandle.readline()
                # remove old file
                v.unlink()
                # rename new file to old
                os.link(nf.name, v)
                # set mode to whatever it was
                v.chmod(mode)
            # we're done
            print(f"  Shebang converted to '{shebang.decode()}': {bfile}")
