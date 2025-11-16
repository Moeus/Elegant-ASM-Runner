data segment
    ; 在此处定义数据
    msg db 30,40,50
data ends

code segment
    assume cs:code, ds:data

start:
    ; 初始化数据段寄存器
    mov ax, data
    mov ds, ax
    mov cx,length msg
print_loop:
    ; === 在此处编写你的程序逻辑 ===
    mov ah, 02h          ; DOS 功能
    mov dl, msg[cx-1]    ; dx 指向字符串地址
    int 21h              ; 调用 DOS 中断
    lopp print_loop

    ; 正常退出程序
    mov ah, 4Ch
    int 21h

code ends
end start