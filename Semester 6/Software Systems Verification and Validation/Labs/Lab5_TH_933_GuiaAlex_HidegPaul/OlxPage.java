package org.example.pages;

import net.serenitybdd.core.annotations.findby.By;
import net.serenitybdd.core.annotations.findby.FindBy;
import net.serenitybdd.core.pages.WebElementFacade;
import net.thucydides.core.annotations.DefaultUrl;
import net.thucydides.core.pages.PageObject;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebElement;

import java.util.List;
import java.util.stream.Collectors;

@DefaultUrl("https://www.olx.ro/")
public class OlxPage extends PageObject {
    @FindBy(id = "search")
    private WebElementFacade searchTerms;

    @FindBy(name = "searchBtn")
    private WebElementFacade lookupButton;

    public void enter_keywords(String keyword) {
        searchTerms.type(keyword);
    }

    public void lookup_terms() {
        searchTerms.sendKeys(Keys.ENTER);
    }

    public boolean filter_results(String filter) {
        List<WebElementFacade> list = findAll(By.className("css-szrfjb"));
        WebElement filterButton = list.stream()
                .map(element -> element.findElements(By.tagName("a")))
                .flatMap(List::stream)
                .filter(s -> s.getText().toLowerCase().contains(filter.toLowerCase()))
                .findFirst()
                .orElse(null);
        if (filterButton != null) {
            WebElement cookieButton = find(By.id("onetrust-button-group")).findElement(By.id("onetrust-accept-btn-handler"));
            cookieButton.click();
//            evaluateJavascript("window.scrollBy(0, 500)");
            filterButton.click();
            return true;
        } else {
            return false;
        }
    }

    public List<String> get_products(String productName) {
        WebElementFacade resultList = find(By.className("css-j0t2x2"));
        return resultList.findElements(By.className("css-u2ayx9")).stream()
                .map(element -> element.findElement(By.tagName("a")))
                .map(WebElement::getText)
                .filter(s -> s.toLowerCase().contains(productName.toLowerCase()))
                .collect(Collectors.toList());
    }
}
