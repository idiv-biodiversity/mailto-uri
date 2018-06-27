# -----------------------------------------------------------------------------
# mailto-uri - creates mailto URIs
#
# Copyright (C) 2018 Christian Krause
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
# -----------------------------------------------------------------------------

import argparse
import sys
import urllib.parse

def main():

    # -------------------------------------------------------------------------
    # command line arguments
    # -------------------------------------------------------------------------

    parser = argparse.ArgumentParser()

    parser.add_argument('body',
                        help = 'mail body input file')

    parser.add_argument('-r', '--recipient', required = True,
                        help = 'mail recipient')

    parser.add_argument('-s', '--subject', required = True,
                        help = 'mail subject')

    args = parser.parse_args()

    # -------------------------------------------------------------------------
    # app
    # -------------------------------------------------------------------------

    if args.body and args.body != '-':
        input = open(args.body)
    else:
        input = sys.stdin

    data = bytes(input.read(), input.encoding)

    if args.body and args.body != '-':
        input.close()

    subject = urllib.parse.quote(args.subject)

    body = urllib.parse.quote(data)

    # -------------------------------------------------------------------------
    # output
    # -------------------------------------------------------------------------

    print('mailto:{}?subject={}&body={}'.format(args.recipient, subject, body))
