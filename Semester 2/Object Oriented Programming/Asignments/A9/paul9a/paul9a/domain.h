#pragma once
#include <string>
#include <iostream>

class Tutorial
{
private:
	std::string title;
	std::string presenter;
	std::string duration;
	size_t likes;
	std::string link;

public:
	/// <summary>
	/// Default constructor for the Tutorial class
	/// </summary>
	Tutorial();

	/// <summary>
	/// Constructor for the tutorial class with initializers for all fields
	/// </summary>
	/// <param name="title">The title of tutorial</param>
	/// <param name="presenter">The presenter of the tutorial</param>
	/// <param name="duration">The duration of the tutorial</param>
	/// <param name="likes">The number of likes of the tutorial</param>
	/// <param name="link">The link of the tutorial</param>
	Tutorial(std::string title, std::string presenter, std::string duration, size_t likes, std::string link);

	/// <summary>
	/// Destructor for the tutorial
	/// </summary>
	~Tutorial();

	/// Getters
	std::string GetTitle() const;
	std::string GetPresenter() const;
	std::string GetDuration() const;
	size_t GetLikes() const;
	std::string GetLink() const;

	/// Setters
	void SetTitle(std::string title);
	void SetPresenter(std::string presenter);
	void SetDuration(std::string durationoftutorial);
	void SetLikes(size_t likes);
	void SetLink(std::string link);

	/// <summary>
	/// Equality operator for the tutorial class
	/// </summary>
	/// <param name="other">The tutorial to compare the current object with</param>
	/// <returns>True if the tutorials are identical, false otherwise</returns>
	bool operator==(const Tutorial& other) const;

	/// <summary>
	/// Insertion operator for the tutorial class
	/// </summary>
	/// <param name="os">The stream object to write the data of the tutorial to</param>
	/// <param name="is">The tutorial whose fields will be written</param>
	/// <returns>A stream object which contains the data of the tutorial</returns>
	friend std::ostream& operator<<(std::ostream& os, const Tutorial& t);
	friend std::istream& operator>>(std::istream& is, Tutorial& tutorial);
	friend class TutorialTests;

};

class TutorialTests
{
public:
	static void TestAllTutorial();
	static void TestConstructorsAndGettersTutorial();
	static void TestSettersTutorial();
	static void TestEqualityTutorial();
	static void TestExtractionOperator();
};