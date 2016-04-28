def parse_section_headings(f):

    headings = []

    targets = [line.strip('#').strip()
               for line in open(f)
               if line.find('#') == 0] 

    return targets

