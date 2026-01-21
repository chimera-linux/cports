from cbuild.core import paths

import os
import ssl
import math
import hashlib
import pathlib
import threading
from time import time as timer
from urllib import request
from http.client import responses
from multiprocessing.pool import ThreadPool


def get_cksum(dfile, pkg):
    with dfile.open("rb") as fn:
        return hashlib.file_digest(fn, "sha256").hexdigest()


def make_link(dfile, cksum):
    shapath = paths.sources() / "by_sha256"
    linkpath = shapath / f"{cksum}_{dfile.name}"
    if not linkpath.is_file():
        shapath.mkdir(parents=True, exist_ok=True)
        linkpath.hardlink_to(dfile)
    else:
        tino = linkpath.stat().st_ino
        sino = dfile.stat().st_ino
        # if inodes differ, make sure to sync it
        if tino != sino:
            linkpath.unlink()
            linkpath.hardlink_to(dfile)


def verify_cksum(dfile, idx, pkg):
    cksum = pkg.sha256[idx]
    pkg.log(f"verifying sha256sums for source '{dfile.name}'... ", "")
    filesum = get_cksum(dfile, pkg)
    if cksum != filesum:
        if pkg.accept_checksums:
            pkg.logger.out_plain("")
            pkg.logger.out(f"\f[orange]SHA256 UPDATED: {cksum} -> {filesum}")
            pkg.sha256[idx] = filesum
            return True
        else:
            pkg.logger.out_plain("")
            pkg.logger.out(
                f"\f[red]SHA256 mismatch for '{dfile.name}':\n{filesum}"
            )
            return False
    else:
        make_link(dfile, cksum)
        pkg.logger.out_plain("OK.")
        return True


def link_cksum(dfile, cksum, pkg):
    # it's already in the destination, don't try to link
    if dfile.is_file():
        return True
    shapath = paths.sources() / "by_sha256"
    linkpath = shapath / f"{cksum}_{dfile.name}"
    if len(cksum) > 0 and linkpath.is_file():
        dfile.hardlink_to(linkpath)
        pkg.log(f"using known source '{dfile.name}'")
        # do an early verify in case the known source is corrupt
        if not verify_cksum(dfile, cksum, pkg):
            pkg.log_warn(f"corrupt by_sha256 entry '{dfile.name}' - removing")
            linkpath.unlink()
            dfile.unlink()
            return False
        else:
            return True
    else:
        return False


def get_nameurl(pkg, d):
    if d.startswith("!"):
        d = d[1:]
    bkt = d.rfind(">")
    bsl = d.rfind("/")
    if bkt < 0 and bsl < 0:
        pkg.error(f"source '{d}' has an invalid format")
    if bkt > bsl:
        return d[0:bkt], d[bkt + 1 :]
    else:
        return d, d[bsl + 1 :]


fmtx = threading.Lock()
fstatus = []
flens = []
fctx = None


def fetch_stream(url, dfile, dhdrs, ehdrs, idx, ntry, rqf, rbuf):
    # ensure the response if what we expect, otherwise error
    # it may be None for FTP and so on though
    if rqf.status is not None:
        match int(rqf.status):
            case 200 | 206:
                pass
            case _:
                status = responses[int(rqf.status)]
                return url, dfile, f"unexpected status: {status}"
    # if resuming fetch the known length
    if ntry > 0:
        with fmtx:
            clen = flens[idx]
            if int(rqf.status) != 206:
                # range ignored/not supported, do a normal retry
                fmode = "wb"
                fstatus[idx] = 0
                if ntry > 3:
                    # don't iterate forever
                    return (
                        url,
                        dfile,
                        "incomplete file, fetch attempts exceeded",
                    )
            else:
                fmode = "ab"
                # reset the counter, we allow unlimited chunks
                ntry = 0
    else:
        fmode = "wb"
        if rqf.status is not None:
            clen = rqf.getheader("content-length")
            if clen:
                clen = int(clen)
                with fmtx:
                    flens[idx] = clen
        else:
            clen = None
    # regardless, make a buffer
    if clen and not rbuf:
        rbuf = bytearray(max(65536, clen // 100))
    else:
        rbuf = bytearray(65536)
    dores = False
    pfile = dfile.with_name(dfile.name + ".part")
    with open(pfile, fmode) as df:
        while True:
            nread = rqf.readinto(rbuf)
            if nread == 0:
                break
            if nread < len(rbuf):
                df.write(rbuf[0:nread])
            else:
                df.write(rbuf)
            with fmtx:
                fstatus[idx] += nread
        with fmtx:
            # if we know the final content-length and we receive less than
            # that in the body, resume the request with a range header set
            if clen and fstatus[idx] != clen:
                dores = True
            else:
                # otherwise just mark the file at 100%
                flens[idx] = fstatus[idx]
    # resume outside the mutex
    if dores:
        rqf.close()
        return fetch_url(url, dfile, dhdrs, ehdrs, idx, ntry + 1, rbuf)
    # rename and return
    pfile.rename(dfile)
    return None, None, None


def fetch_url(url, dfile, dhdrs, ehdrs, idx, ntry, rbuf=None):
    try:
        hdrs = dict(dhdrs)
        if ehdrs:
            hdrs.update(ehdrs)
        # delete none values in case we have them
        for k in hdrs:
            if hdrs[k] is None:
                del hdrs[k]
        if ntry > 0:
            with fmtx:
                hdrs["Range"] = f"bytes={fstatus[idx]}-{flens[idx]}"
        rq = request.Request(
            url,
            data=None,
            headers=hdrs,
        )
        with request.urlopen(rq, context=fctx) as rqf:
            return fetch_stream(url, dfile, dhdrs, ehdrs, idx, ntry, rqf, rbuf)
    except Exception as e:
        if ntry > 3:
            return url, dfile, str(e)
        # try a few times on failures
        return fetch_url(url, dfile, dhdrs, ehdrs, idx, ntry + 1, rbuf)


def invoke(pkg):
    global fstatus, flens, fctx

    srcdir = paths.sources() / f"{pkg.pkgname}-{pkg.pkgver}"

    dfgood = 0
    errors = 0

    dhdrs = {
        "User-Agent": "cbuild-fetch/4.20.69",
        "Accept": "*/*",
    }
    ehdrs = os.getenv("CBUILD_FETCH_HEADERS")
    if ehdrs:
        for hdr in ehdrs.split("\n"):
            hdrl = hdr.split(":")
            if len(hdrl) != 2:
                pkg.error(f"invalid request header: '{hdr}'")
            dhdrs[hdrl[0].strip().title()] = hdrl[1].lstrip()

    caenv = os.getenv("CBUILD_FETCH_CAFILE")
    if caenv:
        capath = pathlib.Path(caenv)
    else:
        # if bldroot exists and we have a cert bundle, use it
        capath = paths.bldroot() / "etc/ssl/certs.pem"

    # if we have a valid ca file, create a context for it
    if capath.is_file():
        fctx = ssl.create_default_context(cafile=capath)
    else:
        fctx = None

    if len(pkg.source) != len(pkg.sha256):
        pkg.error("sha256sums do not match sources")

    if not pkg.source_headers:
        shdrs = [None] * len(pkg.source)
    else:
        shdrs = pkg.source_headers

    if len(pkg.source) != len(shdrs):
        pkg.error("source_headers must match sources")

    if not srcdir.is_dir():
        try:
            srcdir.mkdir(parents=True)
            os.chown(srcdir, -1, os.getgid(), srcdir)
        except Exception:
            pass

    if not srcdir.is_dir():
        pkg.error(f"'{srcdir}' is not a directory")

    for dc in zip(pkg.source, pkg.sha256):
        d, ck = dc
        url, fname = get_nameurl(pkg, d)
        dfile = srcdir / fname
        if dfile.is_file():
            filesum = get_cksum(dfile, pkg)
            if ck == filesum:
                make_link(dfile, filesum)
                dfgood += 1
            else:
                pkg.log_warn(f"wrong sha256 found for {fname} - purging")
                dfile.unlink()

    if len(pkg.source) == dfgood:
        return

    tofetch = []
    dfiles = []
    # reset (could be filled from previous bulk)
    fstatus = []
    flens = []

    for dc in zip(pkg.source, shdrs, pkg.sha256):
        d, hdrs, ck = dc
        url, fname = get_nameurl(pkg, d)
        dfile = srcdir / fname
        if not link_cksum(dfile, ck, pkg):
            idx = len(tofetch)
            tofetch.append((url, dfile, hdrs, idx))
            fstatus.append(0)
            flens.append(-1)
            pkg.log(f"fetching source '{fname}'...")
            dfiles.append((dfile, ck))

    def do_fetch_url(mv):
        url, dfile, hdrs, idx = mv
        return fetch_url(url, dfile, dhdrs, hdrs, idx, 0)

    # max 16 connections
    tpool = ThreadPool(16)
    dretr = tpool.map_async(do_fetch_url, tofetch)
    ferrs = 0
    # progress while processing
    start = timer()
    # wait up to a second first
    dretr.wait(1)
    printed = False
    maxlen = 0
    # now loop
    while not dretr.ready():
        # go up as many lines as we previously printed
        if printed:
            for nl in range(len(tofetch)):
                pkg.logger.out_raw("\033[A")
        # take a lock and make up status array for all sources
        with fmtx:
            for url, dfile, hdrs, idx in tofetch:
                dled = fstatus[idx]
                clen = flens[idx]
                # compute percetnage if we can (known content-length)
                if clen < 0:
                    prog = "unknown%"
                else:
                    percent = math.floor((dled / clen) * 100)
                    prog = f"{percent}%"
                # we can always compute speed
                speed = dled / (timer() - start)
                unit = "B/s"
                # provide more useful units
                if speed > 1024:
                    speed /= 1024
                    if speed > 1024:
                        speed /= 1024
                        unit = "MB/s"
                    else:
                        unit = "kB/s"
                # print with speed up to 1 decimal digit
                if pkg.logger.use_colors:
                    if dled == clen:
                        pstr = f"[done {dfile.name}]"
                    else:
                        pstr = f"[{prog} {dfile.name} ({speed:.1f} {unit})]"
                    if len(pstr) >= maxlen:
                        maxlen = len(pstr)
                    else:
                        pstr += " " * (maxlen - len(pstr))
                    pkg.logger.out_raw(pstr + "\n")
        # wait up to a second
        dretr.wait(1)
        if pkg.logger.use_colors:
            printed = True
    # at this point all tasks have finished, check the results
    for url, dfile, err in dretr.get():
        if url:
            pkg.log_warn(f"error fetching '{dfile.name}' ({url}): {err}")
            ferrs += 1
    # error if something failed to fetch
    if ferrs > 0:
        pkg.error(f"failed to fetch {ferrs} sources")
    # verify the sources
    for idx, [dfile, _] in enumerate(dfiles):
        if not dfile.is_file():
            pkg.error(f"source '{dfile}' does not exist")
        if not verify_cksum(dfile, idx, pkg):
            errors += 1
    # error if something failed to verify
    if errors > 0:
        pkg.error(
            f"failed to verify {errors} sources",
            hint="use 'cbuild prepare-upgrade' to update checksums",
        )
