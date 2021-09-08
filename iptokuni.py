#!/usr/bin/env python

import datetime
import ipaddress
import os
import sys

import geoip2.database


def init_mmdb(path):
    if os.path.exists(path):
        return geoip2.database.Reader(path)
    else:
        print(f"No such file: {path}")
        sys.exit(1)


def ip_to_country():
    reader = init_mmdb("./GeoLite2-City.mmdb")
    print(
        f"build_date: {datetime.datetime.fromtimestamp(reader.metadata().build_epoch)}"
    )

    def func(ip):
        print(f"{ip}: {reader.city(ip).country.iso_code}")

    return func


def subnet_to_iplist(ip_subnet):
    return list(ipaddress.ip_network(ip_subnet, strict=False).hosts())


def main():
    func = ip_to_country()
    if not sys.stdin.isatty():
        for ip in sys.stdin:
            func(ip.strip("\n"))
    else:
        argv = sys.argv[1]
        if "/" in argv:
            if argv.split("/")[1] != "32":
                for ip in subnet_to_iplist(sys.argv[1]):
                    func(ip)
            else:
                func(argv.split("/")[0])
        else:
            func(argv)


if __name__ == "__main__":
    main()
