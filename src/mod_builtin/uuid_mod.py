#!/usr/bin/env python
# -*- coding: utf-8 -*-

import uuid

# 基于MAC地址生成UUID，不安全
print('uuid1=>', uuid.uuid1())

# 基于名称空间和名字的MD5值生成UUID
print('uuid3=>', uuid.uuid3(uuid.NAMESPACE_DNS, 'hello'))

# 生成随机UUID
print('uuid4=>', uuid.uuid4())

# 基于名称空间和名字的SHA-1值生成UUID
print('uuid5=>', uuid.uuid5(uuid.NAMESPACE_URL, 'hello'))

# 指定参数生成UUID
print('Custom UUID=>')
print(uuid.UUID('{12345678-1234-5678-1234-567812345678}'))
print(uuid.UUID('12345678123456781234567812345678'))
print(uuid.UUID('urn:uuid:12345678-1234-5678-1234-567812345678'))
print(uuid.UUID(bytes=b'\x12\x34\x56\x78' * 4))
print(uuid.UUID(bytes_le=b'\x78\x56\x34\x12\x34\x12\x78\x56' +
                         b'\x12\x34\x56\x78\x12\x34\x56\x78'))
print(uuid.UUID(fields=(0x12345678, 0x1234, 0x5678, 0x12, 0x34, 0x567812345678)))
print(uuid.UUID(int=0x12345678123456781234567812345678))

print('\n常见属性')
u = uuid.uuid4()
print('UUID: ', u)
print('UUID.bytes: ', u.bytes)
print('UUID.bytes_le: ', u.bytes_le)
print('UUID.fields: ', u.fields)
print('UUID.hex: ', u.hex)
print('UUID.int: ', u.int)
print('UUID.variant: ', u.variant)
print('UUID.version: ', u.version)
print('UUID.is_safe: ', u.is_safe)
print('getnode: ', uuid.getnode())   # 本机MAC地址
