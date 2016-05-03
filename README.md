#email_validator
 Check e-mail for compliance with the following rules:
 
1. e-mail consists of a name and a domain part, the parts are separated by a "@";
2. The domain part is not shorter than three characters and no longer than 256, is a
set of non-empty strings of characters a-z 0-9_- and separated by a point;
3. Each domain component part can not begin or end with a "-";
4. The name (before the @) does not exceed 128 characters, consists of the characters
a-z0-9 "._-;
5. in the name are not allowed two consecutive points;
6. if the name has double quotes ", they must be paired;
7. The name may occur in the characters "!,:", but only between the paired double quotes.
 
Unit test check the correct e-mail
