print("---------Practise 2-3\n")

_name_ = "eric"
message1 = f"Hello {_name_}, would you like to learn some python today? "
print(message1)

print("\n---------Practise 2-4\n")

message2 = f"Hello {_name_.title()}, would you like to learn some python today? "
print(message2)

message3 = f"Hello {_name_.lower()}, would you like to learn some python today? "
print(message3)

message4 = f"Hello {_name_.upper()}, would you like to learn some python today? "
print(message4)

print("\n---------Practise 2-5\n")
# Solution A
_quote_ = '"A person who never made a mistake never tried anything new."'
print(f"Albert Einstein once said, {_quote_}")

# Solution B
_quote_ = "A person who never made a mistake never tried anything new."
print(f'Albert Einstein once said, "{_quote_}"')

# Solution C
_quote_ = "A person who never made a mistake never tried anything new."
print(f'Albert Einstein once said, \"{_quote_}\"')

print("\n---------Practise 2-6\n")
famous_person1 = "Albert Einstein"
_quote_ = '"A person who never made a mistake never tried anything new."'
print(f"{famous_person1} once said, {_quote_}")

print("\n---------Practise 2-7\n")
famous_person2 = " albert Einstein "
_quote_ = '"A person who never made a mistake never tried anything new."'
print(f"{famous_person2.upper()} once said, {_quote_}")
print(f"{famous_person2.lower()} once said, {_quote_}")
print(f"{famous_person2.lstrip()} once said, {_quote_}")
print(f"{famous_person2.rstrip()} once said, {_quote_}")
print(f"{famous_person2.strip()} once said, {_quote_}")
print(f"{famous_person2.strip().title()} once said, {_quote_}")