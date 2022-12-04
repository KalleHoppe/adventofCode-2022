// See https://aka.ms/new-console-template for more information
Console.WriteLine("Advent of code Day 1 b");
var filePath = @"C:\Repos\advent22\1\b\advent22-1b\input.txt";
var allCals = new List<int>();
var currSum = 0;

foreach (var line in File.ReadAllLines(filePath))
{
    if (!string.IsNullOrWhiteSpace(line))
    {
        currSum = currSum + int.Parse(line);
        continue;
    }
        allCals.Add(currSum);
        currSum = 0;
    
}

var top3 = allCals.OrderByDescending(x => x).Take(3);
var sum = top3.Sum();
foreach (var cal in top3)
{
    Console.WriteLine($"The top three had {cal} cals");
}

Console.WriteLine("------------------------------------");
Console.WriteLine($"The sum of the top three is {sum}");
Console.ReadLine();
