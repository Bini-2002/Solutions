def split_and_join(line):
    new = line.split(' ')
    
    final = "-".join(new)
    
    return final
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)