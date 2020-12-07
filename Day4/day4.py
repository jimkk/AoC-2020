import re


with open("input.txt", "r") as file:
    rawdata = file.read()

passports = rawdata.split("\n\n")
passports = [a.replace('\n', ' ').replace('  ', '') for a in passports]

passport_fields = [{v.split(':')[0] : v.split(':')[1] for v in set(re.findall(r'([a-z]{3}:[a-z0-9#]+)', a))} for a in passports]
passport_field_counts = [len(a.keys()) - ('cid' in a.keys()) for a in passport_fields]

print('Part 1: ' + str(sum([1 for a in passport_field_counts if a > 6])))

def valid(i):
    key = i[0]
    value = i[1]
    if key == 'byr':
        year = int(value)
        return (year >= 1920 and year <= 2002)
    elif key == 'iyr':
        year = int(value)
        return (year >= 2010 and year <= 2020)
    elif key == 'eyr':
        year = int(value)
        return (year >= 2020 and year <= 2030)
    elif key == 'hgt':
        value = re.findall(r'([0-9]{3}cm|[0-9]{2}in)', value)
        if not value: 
            return False
        value = value[0]
        value = [value[:-2], value[-2:]]
        height = int(value[0])
        if value[1] == 'cm':
            return (height >= 150 and height <= 193)
        if value[1] == 'in':
            return (height >= 59 and height <= 76)
        return False
    elif key == 'hcl':
        return re.match(r'#[0-9a-f]{6}', value) != None
    elif key == 'ecl':
        return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    elif key == 'pid':
        return re.match(r'^[0-9]{9}$', value) != None
    return False

valid_passport_fields = [p for p in passport_fields if sum(map(valid, p.items())) > 6]
print('Part 2: ' + str(len(valid_passport_fields)))

