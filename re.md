# 1. re.match函数

语法：re.match(pattern, string, flags=0)

|         |                 含义                 |
| :-----: | :----------------------------------: |
| pattern |           匹配的正则表达式           |
| string  |            要匹配的字符串            |
|  flags  | 标志位，用于控制正则表达式的匹配方式 |

```
re.I  忽略大小写
re.L  表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
re.M  多行模式
re.S  即为 . 并且包括换行符在内的任意字符（. 不包括换行符）
re.U  表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
re.X  为了增加可读性，忽略空格和 # 后面的注释
```

### 1.1 匹配单个字符

<table align="center" cellspacing="0"><tbody><tr><td style="vertical-align:middle;width:54pt;"><span style="color:#000000;">字符</span></td><td style="vertical-align:middle;width:364px;"><span style="color:#000000;">功能</span></td><td style="vertical-align:middle;width:628px;">位置</td></tr><tr><td style="vertical-align:middle;"><span style="color:#000000;">.</span></td><td style="vertical-align:middle;width:364px;"><span style="color:#000000;">匹配任意1个字符（除了\n）</span></td><td style="vertical-align:middle;width:628px;"></td></tr><tr><td style="vertical-align:middle;"><span style="color:#000000;">[<span style="color:#000000;"> ]</span></span></td><td style="vertical-align:middle;width:364px;"><span style="color:#000000;">匹配[ ]中列举的字符</span></td><td style="vertical-align:middle;width:628px;"></td></tr><tr><td style="vertical-align:middle;"><span style="color:#000000;">\d</span></td><td style="vertical-align:middle;width:364px;"><span style="color:#000000;">匹配数字，即0-9</span></td><td style="vertical-align:middle;width:628px;">可以写在字符集[...]中</td></tr><tr><td style="vertical-align:middle;"><span style="color:#000000;">\D</span></td><td style="vertical-align:middle;width:364px;"><span style="color:#000000;">匹配⾮数字，即不是数字</span></td><td style="vertical-align:middle;width:628px;">可以写在字符集[...]中</td></tr><tr><td style="vertical-align:middle;"><span style="color:#000000;">\s</span></td><td style="vertical-align:middle;width:364px;"><span style="color:#000000;">匹配空⽩，即空格，tab键</span></td><td style="vertical-align:middle;width:628px;">可以写在字符集[...]中</td></tr><tr><td style="vertical-align:middle;"><span style="color:#000000;">\S</span></td><td style="vertical-align:middle;width:364px;"><span style="color:#000000;">匹配⾮空⽩字符</span></td><td style="vertical-align:middle;width:628px;">可以写在字符集[...]中</td></tr><tr><td style="vertical-align:middle;"><span style="color:#000000;">\w</span></td><td style="vertical-align:middle;width:364px;"><span style="color:#000000;">匹配单词字符，即a-z、A-Z、0-9、_</span></td><td style="vertical-align:middle;width:628px;">可以写在字符集[...]中</td></tr><tr><td style="vertical-align:middle;"><span style="color:#000000;">\W</span></td><td style="vertical-align:middle;width:364px;"><span style="color:#000000;">匹配⾮单词字符</span></td><td style="vertical-align:middle;width:628px;">可以写在字符集[...]中</td></tr><tr><td style="vertical-align:middle;"><span style="color:#000000;">\w</span></td><td style="vertical-align:middle;width:364px;"><span style="color:#000000;">\w 匹配单词字符，即a-z、A-Z、0-9、_</span></td><td style="vertical-align:middle;width:628px;"></td></tr><tr><td style="vertical-align:middle;"><span style="color:#000000;">\W</span></td><td style="vertical-align:middle;width:364px;"><span style="color:#000000;">匹配⾮单词字符</span></td><td style="vertical-align:middle;width:628px;"></td></tr></tbody></table>

实例：re.match1.py

### 1.2 匹配多个字符

<table align="center" cellspacing="0"><tbody><tr><td style="vertical-align:middle;width:54pt;">字符</td><td style="vertical-align:middle;width:469px;">功能</td><td style="vertical-align:middle;width:142px;">位置</td><td style="vertical-align:middle;width:1px;">表达式实例</td><td style="vertical-align:middle;width:120px;">完整匹配的字符串</td></tr><tr><td style="vertical-align:middle;width:54pt;"><span style="color:#000000;">*</span></td><td style="vertical-align:middle;width:469px;"><span style="color:#000000;">匹配前⼀个字符出现0次或者⽆限次，即可有可⽆</span></td><td style="vertical-align:middle;width:142px;">用在字符或(...)之后</td><td style="vertical-align:middle;width:1px;">abc*</td><td style="vertical-align:middle;width:120px;">abccc</td></tr><tr><td style="vertical-align:middle;"><span style="color:#000000;">+</span></td><td style="vertical-align:middle;width:469px;"><span style="color:#000000;">匹配前⼀个字符出现1次或者⽆限次，即⾄少有1次</span></td><td style="vertical-align:middle;width:142px;">用在字符或(...)之后</td><td style="vertical-align:middle;width:1px;">abc+</td><td style="vertical-align:middle;width:120px;">abccc</td></tr><tr><td style="vertical-align:middle;"><span style="color:#000000;">?</span></td><td style="vertical-align:middle;width:469px;"><span style="color:#000000;">匹配前⼀个字符出现1次或者0次，即要么有1次，要么没有</span></td><td style="vertical-align:middle;width:142px;">用在字符或(...)之后</td><td style="vertical-align:middle;width:1px;">abc?</td><td style="vertical-align:middle;width:120px;">ab,abc</td></tr><tr><td style="vertical-align:middle;"><span style="color:#000000;">{m}</span></td><td style="vertical-align:middle;width:469px;"><span style="color:#000000;">匹配前⼀个字符出现m次</span></td><td style="vertical-align:middle;width:142px;">用在字符或(...)之后</td><td style="vertical-align:middle;width:1px;">ab{2}c</td><td style="vertical-align:middle;width:120px;">abbc</td></tr><tr><td style="vertical-align:middle;"><span style="color:#000000;">{m,n}</span></td><td style="vertical-align:middle;width:469px;"><span style="color:#000000;">匹配前⼀个字符出现从m到n次，若省略m，则匹配0到n次，若省略n，则匹配m到无限次</span></td><td style="vertical-align:middle;width:142px;">用在字符或(...)之后</td><td style="vertical-align:middle;width:1px;">ab{1,2}c</td><td style="vertical-align:middle;width:120px;">abc,abbc</td></tr></tbody></table>

实例：re.match2.py

### 1.3 **匹配开头结尾**

<table align="center" cellspacing="0" style="width:500pt;"><tbody><tr><td style="vertical-align:middle;width:54pt;"><span style="color:#000000;">字符</span></td><td style="vertical-align:middle;width:54pt;"><span style="color:#000000;">功能</span></td></tr><tr><td style="vertical-align:middle;"><span style="color:#000000;">^</span></td><td style="vertical-align:middle;"><span style="color:#000000;">匹配字符串开头</span></td></tr><tr><td style="vertical-align:middle;"><span style="color:#000000;">$</span></td><td style="vertical-align:middle;"><span style="color:#000000;">匹配字符串结尾</span></td></tr></tbody></table>

实例：re.match3.py

### 1.4 **匹配分组**

<table align="center" cellspacing="0"><tbody><tr><td style="vertical-align:middle;width:230px;"><span style="color:#000000;">字符</span></td><td style="vertical-align:middle;"><span style="color:#000000;">功能</span></td><td style="vertical-align:middle;"><span style="color:#000000;">实例</span></td></tr><tr><td style="vertical-align:middle;width:230px;"><span style="color:#000000;">|</span></td><td style="vertical-align:middle;"><span style="color:#000000;">匹配左右任意⼀个表达式</span></td><td style="vertical-align:middle;"><span style="color:#000000;"> re.match4.py</span></td></tr><tr><td style="vertical-align:middle;width:230px;"><span style="color:#000000;">(ab)</span></td><td style="vertical-align:middle;"><span style="color:#000000;">将括号中字符作为⼀个分组</span></td><td style="vertical-align:middle;"><span style="color:#000000;"> re.match5.py</span></td></tr><tr><td style="vertical-align:middle;width:230px;"><span style="color:#000000;">\num</span></td><td style="vertical-align:middle;"><span style="color:#000000;">引⽤分组num匹配到的字符串</span></td><td style="vertical-align:middle;"><span style="color:#000000;"> re.match6.py</span></td></tr><tr><td style="vertical-align:middle;width:230px;"><span style="color:#000000;">(?P&lt;name&gt;)</span></td><td style="vertical-align:middle;"><span style="color:#000000;">分组起别名，</span>匹配到的子串组在外部是通过定义的 <em>name</em> 来获取的</td><td style="vertical-align:middle;"><span style="color:#000000;"> re.match7.py</span></td></tr><tr><td style="vertical-align:middle;width:230px;"><span style="color:#000000;">(?P=name)</span></td><td style="vertical-align:middle;"><span style="color:#000000;">引⽤别名为name分组匹配到的字符串</span></td><td style="vertical-align:middle;"><span style="color:#000000;"> re.match8.py</span></td></tr></tbody></table>

# 2. re.compile 函数

 compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。 

```html
prog = re.compile(pattern)
result = prog.match(string)
```

等价于

```html
result = re.match(pattern, string)
```

1. group([group1, …]) 方法  用于获得一个或多个分组匹配的字符串，当要获得整个匹配的子串时，可直接使用 group() 或 group(0)；
2. start([group]) 方法  用于获取分组匹配的子串在整个字符串中的起始位置（子串第一个字符的索引），参数默认值为 0；
3. end([group]) 方法  用于获取分组匹配的子串在整个字符串中的结束位置（子串最后一个字符的索引+1），参数默认值为 0；
4. span([group]) 方法  返回 (start(group), end(group))
5. 实例 re_compile.py

# 3. re.search 函数

re.search 扫描整个字符串并返回第一个成功的匹配，如果没有匹配，就返回一个 None。

re.match与re.search的区别：re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配

# 4. re.findall函数

在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。注意： match 和 search 是匹配一次 findall 匹配所有。

# 5. re.finditer函数

和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。

# 6. re.sub函数

sub是substitute的所写，表示替换，将匹配到的数据进⾏替换。

语法：re.sub(pattern, repl, string, count=0, flags=0)

<table align="center" border="1" cellpadding="1" cellspacing="1" style="width:500px;"><tbody><tr><td>参数</td><td>描述</td></tr><tr><td>pattern</td><td>必选，表示正则中的模式字符串</td></tr><tr><td>repl</td><td>必选，就是replacement，要替换的字符串，也可为一个函数</td></tr><tr><td>string</td><td>必选，被替换的那个string字符串</td></tr><tr><td>count</td><td>可选参数，<em>count</em> 是要替换的最大次数，必须是非负整数。如果省略这个参数或设为 0，所有的匹配都会被替换</td></tr><tr><td>flag</td><td>可选参数，标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。</td></tr></tbody></table>

# 7. re.subn函数

行为与sub()相同，但是返回一个元组 (字符串, 替换次数)。

re.subn(pattern, repl, string[, count])

返回：(sub(repl, string[, count]), 替换次数)

# 8. re.split函数

根据匹配进⾏切割字符串，并返回⼀个列表。

re.split(pattern, string, maxsplit=0, flags=0)

<table align="center" border="1" cellpadding="1" cellspacing="1" style="width:500px;"><tbody><tr><td>参数</td><td>描述</td></tr><tr><td>pattern</td><td>匹配的正则表达式</td></tr><tr><td>string</td><td>要匹配的字符串</td></tr><tr><td>maxsplit</td><td>分隔次数，maxsplit=1 分隔一次，默认为 0，不限制次数</td></tr></tbody></table>
# 9. python贪婪和非贪婪

Python⾥数量词默认是贪婪的（在少数语⾔⾥也可能是默认⾮贪婪），总是尝试匹配尽可能多的字符；⾮贪婪则相反，总是尝试匹配尽可能少的字符。

例如：正则表达式”ab*”如果用于查找”abbbc”，将找到”abbb”。而如果使用非贪婪的数量词”ab*?”，将找到”a”。

注：我们一般使用非贪婪模式来提取。

在"*","?","+","{m,n}"后⾯加上？，使贪婪变成⾮贪婪。

# 10. r的作用

与大多数编程语言相同，正则表达式里使用”\”作为转义字符，这就可能造成反斜杠困扰。

假如你需要匹配文本中的字符”\”，那么使用编程语言表示的正则表达式里将需要4个反斜杠”\\\\”：前两个和后两个分别用于在编程语言里转义成反斜杠，转换成两个反斜杠后再在正则表达式里转义成一个反斜杠。

Python里的原生字符串很好地解决了这个问题，Python中字符串前⾯加上 r 表示原⽣字符串。


