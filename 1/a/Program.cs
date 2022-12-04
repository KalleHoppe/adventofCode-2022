// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");
var filePath = @".\input.txt";
var mostCals = 0;
var elfNo = 0;
var currElf = 0;
var curSum = 0;
foreach (var line in File.ReadAllLines(filePath))
{
    if(!string.IsNullOrWhiteSpace(line))
    {
        curSum = curSum+int.Parse(line);
    }
    else
    {
        currElf++;
        //new elf
        if (curSum > mostCals){
            mostCals = curSum;
            elfNo = currElf;
            Console.WriteLine($"New leader {elfNo} with {mostCals}");
        }
        curSum = 0;
    }
}

Console.WriteLine($"The elf with most calories is {elfNo} with {mostCals}");
Console.ReadLine();
