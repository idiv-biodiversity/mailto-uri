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

def mailto(subject, recipients, cc, content):
    content = urllib.parse.quote(content)

    if subject:
        subject = urllib.parse.quote(subject)
        subject = '&subject={}'.format(subject)
    else:
        subject = ''

    if not isinstance(recipients, (list,)):
        recipients = [recipients]

    if recipients:
        recipients = ','.join(recipients)
    else:
        recipients = ''

    if not isinstance(cc, (list,)):
        cc = [cc]

    if cc:
        cc = ','.join(cc)
        cc = '&cc={}'.format(cc)
    else:
        cc = ''

    return 'mailto:{}?body={}{}{}'.format(
        recipients,
        content,
        subject,
        cc,
    )

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
        '-c', '--cc',
        action = 'append',
        help = 'secondary, carbon copy recipients',
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

def run(source, args):
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
    elif 'to' in mail:
        recipients = mail['to']
    elif 'recipient' in mail:
        recipients = mail['recipient']
    else:
        recipients = []

    if args.cc:
        cc = args.cc
    elif 'cc' in mail:
        cc = mail['cc']
    else:
        cc = []

    if args.subject:
        subject = args.subject
    elif 'subject' in mail:
        subject = mail['subject']
    else:
        subject = ''

    return mailto(subject, recipients, cc, mail.content)

def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.input:
        sources = args.input
    else:
        sources = ['-']

    for source in sources:
        uri = run(source, args)
        print(uri)
