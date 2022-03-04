txt = "Hello World"[::-1]  # Slice statement [::-1]
print(txt)


def reverse(x):
    return x[::-1]


txt2 = reverse("Hello World")
print(txt2)
