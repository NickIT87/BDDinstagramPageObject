Feature: Authorization in an instagram
#test comment
   Scenario Outline: Check positive data login functionality
     Given I am on authorization page
     Then Login as <username>, <password>
     Then Skip download app
     When The authorization as <username> complete, we check logout function

     Examples: By valid data
     | username  | password |
     | mrfox7315 | ******** |

   Scenario Outline: Check negative data login functionality
     Given I am on authorization page
     Then Login as <username>, <password>
     When The authorization fail, we can see <error_message>

     Examples: By incorrect data
     | username  | password | error_message                                                                                                 |
     | @#$$%($*$ | $#%#$%#$ | Введенное вами имя пользователя не принадлежит аккаунту. Проверьте свое имя пользователя и повторите попытку. |
     | mrfox7315 | #@*$&^#@ | К сожалению, вы ввели неверный пароль. Проверьте свой пароль еще раз.                                         |

   Scenario Outline: Check reset password functionality
     Given I am on authorization page
     Then Click forgot password link
     Then Put user <data>, click captcha, and submit the form

     Examples: By user data
     | data           |
     | fake@gmail.com |
