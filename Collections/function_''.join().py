# ''.join()函数的用法
# 语法: 'sep'.join(seq)
# 参数说明：
# sep：分隔符，可以为空
# seq：要连接的元素序列、字符串、元组、字典
# 上面的语法即：以sep作为分隔符（空），将seq所有的元素合并成一个新的字符串
# 返回值：返回一个以分隔符sep连接各个元素后生成的字符串

c = 'abcghidefjkl'
new_c = list(c)
new_c.sort()
print('1.把new_c列表里面的元素按字母排序后:', new_c)

cc = ' '.join(new_c)
print('2.通过空分隔符把new_c列表里面元素进行分隔,赋值给到cc:', cc)

cc = ','.join(new_c)
print('3.通过,分隔符把new_c列表里面元素进行分隔,赋值给到cc:', cc)

# 1.把new_c列表里面的元素按字母排序后: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
# 2.通过空分隔符把new_c列表里面元素进行分隔,赋值给到cc: abcdefghijkl
# 3.通过,分隔符把new_c列表里面元素进行分隔,赋值给到cc: a,b,c,d,e,f,g,h,i,j,k,l
