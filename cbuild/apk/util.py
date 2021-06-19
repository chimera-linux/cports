def strip_tar_endhdr(data):
    tlen = len(data)
    # length of the initial archive without trailing headers
    dlen = 0
    dbeg = 0
    while True:
        # this should not happen though
        if (tlen - dlen) < 512:
            break
        # try if there's a name
        hname = data[dbeg:dbeg + 100]
        # trailing header
        if hname[0] == 0:
            break
        # header size
        dlen += 512
        # data size, if any
        szb = data[dbeg + 124:dbeg + 136].rstrip(b"\x00")
        if len(szb) > 0:
            # align to 512
            dlen += (int(szb, 8) + 511) & ~511
        # new header start
        dbeg = dlen

    return data[0:dlen]
