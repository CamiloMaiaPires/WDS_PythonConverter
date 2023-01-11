cconfig = open('radio_config_Si4463.h', 'r')

lines = cconfig.readlines()
eraseConditions = [
  '/*!', '/*', '*/', '*', '//', '#ifndef', '#else', '#endif', '#error'
]
for i in range(0, len(lines)):

  #deleting comments and unused c directives
  words = lines[i].lstrip(' ').rstrip('\n').rsplit(' ')
  if ('#define RADIO_CONFIGURATION_DATA_ARRAY { 0 }' in lines[i]):
    break

  #if the first word is valid
  if (not (words[0] in eraseConditions)):
    pyconfig = open('out.py', 'a')
    #if the first word is a define, it will make a list in python
    if (words[0] == '#define'):
      if (words[1] != 'RADIO_CONFIG_H_'):
        pyconfig.write(words[1])
        pyconfig.write(' = ')
        words.pop(0)
        words.pop(0)
        if (',' in words[-2]):
          pyconfig.write('[')
          words.append(']')
        if (words[-1][-1] == 'L'):
          pyconfig.write((''.join(words))[:-1])
        else:
          if (words[0] == '{'):
            words[0] = '['
          pyconfig.write(''.join(words))
        pyconfig.write('\n')
    elif (words[0] == '}'):
      pyconfig.write(']')

    else:
      pyconfig.write(lines[i])

pyconfig.close()
cconfig.close()
