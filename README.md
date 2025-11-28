\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[russian]{babel}

\title{Лабораторная работа №1}
\author{}
\date{}

\begin{document}

\maketitle

\section*{Тема}
Элементы объектно-ориентированного программирования в языке Python

\section*{Цель работы}
Приобретение навыков по работе с классами и объектами при написании программ.

\section*{Задание 1}
Реализовать класс Time с полями:
\begin{itemize}
    \item first - целое положительное число, часы
    \item second - целое положительное число, минуты
\end{itemize}

\textbf{Методы:}
\begin{itemize}
    \item \_\_init\_\_ - инициализация с проверкой корректности
    \item read() - ввод с клавиатуры
    \item display() - вывод на экран
    \item minutes() - приведение времени в минуты
\end{itemize}

Реализовать внешнюю функцию make\_Time()

\section*{Задание 2}
Реализовать класс Account, представляющий банковский счет.

\textbf{Поля:}
\begin{itemize}
    \item Фамилия владельца
    \item Номер счета
    \item Процент начисления
    \item Сумма в рублях
\end{itemize}

\textbf{Операции:}
\begin{itemize}
    \item Смена владельца
    \item Снятие/пополнение средств
    \item Начисление процентов
    \item Конвертация в доллары/евро
    \item Получение суммы прописью
\end{itemize}

\end{document}
