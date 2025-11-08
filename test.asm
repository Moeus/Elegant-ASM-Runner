dseg segment
    hello_str db 'Hello, 8086 asm!', 0Dh, 0Ah, '$'
dseg ends

code segment
    assume cs:code, ds:dseg

start:

    mov ax, dseg
    mov ds, ax

    mov ah, 09h
    mov dx, offset hello_str
    int 21h

    mov ah, 4Ch
    int 21h

code ends
end start

