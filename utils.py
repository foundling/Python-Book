def parse_section_headings(f):

    headings = []

    targets = [line.strip('#').strip()
               for line in open(f)
               if line.find('#') == 0] 

    return targets

if __name__ == '__main__':
    headings = parse_section_headings('templates/chapters/iterables.md')
    for h in headings:
        print h
