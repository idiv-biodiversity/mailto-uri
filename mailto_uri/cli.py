# -----------------------------------------------------------------------------
# mailto-uri - creates mailto URIs
#
# Copyright (C) 2018-2019 Christian Krause
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
import frontmatter
import sys
import urllib.parse

def mailto(subject, recipients, content):
    content = urllib.parse.quote(content)
    subject = urllib.parse.quote(subject)

    if recipients:
        recipients = ','.join(recipients)
    else:
        recipients = ''

    print('mailto:{}?subject={}&body={}'.format(
        recipients,
        subject,
        content
    ))

def create_parser():
    parser = argparse.ArgumentParser(
        description = 'converts an email template to a mailto URI',
    )

    parser.add_argument(
        'input',
        nargs = '*',
        help = 'mail body input file, can include optional arguments in front '
               'matter',
    )

    parser.add_argument(
        '-r', '--recipient',
        action = 'append',
        help = 'primary, main recipients',
    )

    parser.add_argument(
        '-s', '--subject',
        help = 'mail subject',
    )

    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.input:
        sources = args.input
    else:
        sources = ['-']

    for source in sources:
        if source == '-':
            source = sys.stdin
        else:
            source = open(source)

        raw = bytes(source.read(), source.encoding)

        if source != '-':
            source.close()

        mail = frontmatter.loads(raw)

        if args.recipient:
            recipients = args.recipient
        elif 'recipient' in mail:
            recipients = mail['recipient']
        else:
            recipients = []

        if not isinstance(recipients, (list,)):
            recipients = [recipients]

        if args.subject:
            subject = args.subject
        elif 'subject' in mail:
            subject = mail['subject']
        else:
            print("mailto-uri: no subject given", file = sys.stderr)
            exit(1)

        mailto(subject, recipients, mail.content)
