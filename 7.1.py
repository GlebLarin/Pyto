write('n=');
readln(n);
case n of
1:begin
   writeln('Введите a,b');
   readln(a,b);
   write('S=',a*b);
   end;
2:writeln('Введите a,h');
   readln(a,h);
   write('S=',a*(h/2));
   end;
3:writeln('Введите a,b,h');
   readln(a,b,h);
   write('S=',(a+b)*h/2);
   end;
4:writeln('Введите a,b,h');
   readln(a,b,h);
   write('S=',(a+b)*h/2);
   end;
5:
else write('Такого номера нет');
end;
readln;
end.