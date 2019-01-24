namespace ConsoleApp.Exercise
{
  public class A0Paper
  {
    /**
     * Complete problem: https://arena.topcoder.com/#/u/practiceCode/17244/67923/15005/2/331608
     * {A0, A1, A2, ... AN}
     * {1, 2, 4, 8, 16, 32, 64} how paper slicing
     * 
     * {0, 0, 2, 0, 33} // process
     * {0, 0, 2, 16, 1}
     * {0, 0, 10, 0, 0}
     * {0, 5, 0, 0, 0}
     * {2, 1, 0, 0, 0} "possible"
     * 
     * {0, 1, 0, 4, 6, 0, 9} 
     * {0, 1, 2, 0, 6, 0, 9}
     * {0, 2, 0, 0, 6, 0, 9}
     * {1, 0, 0, 0, 6, 0, 9} "possible"
     * 
     * {0,0,0,0,15}
     * {0,0,0,7,1}
     * {0,0,3,1,1}
     * {0,1,1,1,1} "imposible
     * */
    public string canBuild( int[] A )
    {
      bool possible = false;
      if (A.Length>=1 && A.Length <= 21 )
      {
        int pos = 0;
        int temp;

        while( pos >= 0 )
        {
          temp = A[pos];
          if( temp > 0 && pos == 0 )
          {
            possible = true;
            break;
          }
          else if( temp > 1 )
          {
            int check = temp / 2;
            int mod = temp % 2;
            A[pos] = mod;
            A[pos - 1] += check;
            pos--;
          }
          else
          {
            if (pos + 1 >= A.Length ) { possible = false; break; }
            pos++;
          }
        }
      }
      return possible ? "Possible" : "Impossible";
    }
  }
}
