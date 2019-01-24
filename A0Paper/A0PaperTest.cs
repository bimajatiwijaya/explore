using ConsoleApp.Exercise;
using NUnit.Framework;

namespace UnitTestExercise.Nunit
{
  [TestFixture]
  public class A0PaperNunitTest
  {
    [Test]
    public void Test1()
    {
      A0Paper a0Obj = new A0Paper();
      int[] A = { 0, 1, 2 };
      Assert.AreEqual( "Possible", a0Obj.canBuild( A ) );
    }

    [Test]
    public void Test2()
    {
      A0Paper a0Obj = new A0Paper();
      int[] A = { 0, 0, 0, 0, 15 };
      Assert.AreEqual( "Impossible", a0Obj.canBuild( A ) );
    }

    [Test]
    public void Test3()
    {
      A0Paper a0Obj = new A0Paper();
      int[] A = { 2, 0, 0, 0, 0, 0, 0, 3, 2, 0, 0, 5, 0, 3, 0, 0, 1, 0, 0, 0, 5 };
      Assert.AreEqual( "Possible", a0Obj.canBuild( A ) );
    }
  }
}
