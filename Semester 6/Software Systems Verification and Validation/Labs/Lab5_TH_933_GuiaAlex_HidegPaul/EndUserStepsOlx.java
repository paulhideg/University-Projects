package org.example.steps.serenity;

import net.thucydides.core.annotations.Step;
import org.example.pages.OlxPage;

public class EndUserStepsOlx {
    OlxPage olxPage;

    @Step
    public void is_the_home_page() {
        olxPage.open();
    }

    @Step
    public void filter_products(String filter) {
        assert olxPage.filter_results(filter);
    }

    @Step
    public void should_see_products(String productName) {
        assert olxPage.get_products(productName).size() > 0;
    }

    @Step
    public void enters(String keyword) {
        olxPage.enter_keywords(keyword);
    }

    @Step
    public void starts_search() {
        olxPage.lookup_terms();
    }

    @Step
    public void looks_for(String term) {
        enters(term);
        starts_search();
    }
}