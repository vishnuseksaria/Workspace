import java.util.*;

public class RockPaperScissor
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        System.out.println("WELCOME\nThis is score_computer rock paper scissor game.\nThere will be five rounds in this game.\nIf there is score_computer tie, the round will not be counted.\nThe scores will be displayed after each round.\nThe one with greater score will be declared the winner.");
        int n=0,score_computer=0,score_player=0;
        // n indicates round number
        while(n!=5)
        {
            System.out.println("Enter :\n1 for Rock\n2 for Paper\n3 for Scissor");
            System.out.print("Player : ");
            double choice_player = in.nextByte();

            if (choice_player>3 || choice_player<1)
            {
                System.out.println("Invalid choice! Enter again.");
                continue;
            }
            double choice_computer = Math.floor((Math.random()*3)+1);
            System.out.println("Computer : "+(int)choice_computer);

            if(choice_player==1 && choice_computer==2 || choice_player==2 && choice_computer==3 || choice_player==3 && choice_computer==1)
            {
                score_computer++;
                System.out.println("Computer : "+score_computer+" | Player : "+score_player);
            }
            else if(choice_computer==1 && choice_player==2 || choice_computer==2 && choice_player==3 || choice_computer==3 && choice_player==1)
            {
                score_player++;
                System.out.println("Computer : "+score_computer+" | Player : "+score_player);
            }
            else
            {
                System.out.println("Computer : "+score_computer+" | Player : "+score_player);
                continue;
            }
            n++;
        }

        if(score_computer>score_player)
            System.out.println("Computer wins.");
        else
            System.out.println("Player wins.");

        System.out.println("ThankYou for using my game.");
    }
}
