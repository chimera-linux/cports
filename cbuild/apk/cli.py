from cbuild.core import logger, paths

from . import sign

import pathlib
import subprocess

def build_index(repopath, epoch, keypath):
    repopath = pathlib.Path(repopath)

    cmd = ["apk", "index", "--quiet", "--root", str(paths.masterdir())]

    if (repopath / "APKINDEX.tar.gz").is_file():
        cmd += ["--index", "APKINDEX.tar.gz"]

    # if no key is given, just use the final index name
    if not keypath:
        cmd += ["--output", "APKINDEX.tar.gz"]
    else:
        cmd += ["--output", "APKINDEX.unsigned.tar.gz"]

    for f in repopath.glob("*.apk"):
        cmd.append(str(f.name))

    # create unsigned index
    signr = subprocess.run(cmd, cwd = repopath, env = {
        "SOURCE_DATE_EPOCH": str(epoch)
    })
    if signr.returncode != 0:
        logger.get().out_red("Indexing failed!")
        return False

    # we're done if no key is given
    if not keypath:
        return True

    try:
        signhdr = sign.sign(
            keypath, repopath / "APKINDEX.unsigned.tar.gz", epoch
        )
    except:
        return False

    # write signed index
    with open(repopath / "APKINDEX.tar.gz", "wb") as outf:
        outf.write(signhdr)
        with open(repopath / "APKINDEX.unsigned.tar.gz", "rb") as inf:
            while True:
                buf = inf.read(16 * 1024)
                if not buf:
                    break
                outf.write(buf)
        (repopath / "APKINDEX.unsigned.tar.gz").unlink()

    return True
