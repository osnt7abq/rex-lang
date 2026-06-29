# 🦖 Rex Language Specification

Version: 0.1 (Hatchling)

---

## Philosophy

Simple. Fast. Powerful.

Rex is designed to be easy to learn, enjoyable to use, and powerful enough for professional software development.

---

# Official Language Rules

## Variables

- Use `let`
- Use `camelCase`

Example:

```rex
let userName = "Alex"
let age = 18
```

## Constants

Use `const`

```rex
const appName = "Rex"
```

## Functions

Use `func`

```rex
func greet(name) {
    print("Hello " + name)
}
```

## Conditions

Do not use parentheses.

```rex
if age >= 18 {
    print("Adult")
}
```

## Loops

```rex
for i in 1..5 {
    print(i)
}
```

## Output

```rex
print("Hello, Earth")
```

---

More rules will be added as Rex evolves.