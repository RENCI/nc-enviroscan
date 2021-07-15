<template>
  <q-layout view="lhr lpr lfr">
    <!--// Left Drawer Starts-->
    <q-drawer v-model="leftDrawerOpen" show-if-above bordered :content-style="{ backgroundColor: 'rgba(199, 235, 235, 0.5)' }">
      <q-space />
      <q-separator />
      <q-space />
      <q-card class="q-pa-md bg-teal-1" style="max-width: 300px">
        <table class="table is-fullwidth">
          <div v-if="Object.keys(selectedFeatureMedBarBox).length > 0">
            <tr>
              <td>
                <apexchart width="280" type="radialBar" :options="apxmedoptions" :series="selectedFeatureMedBarBox" />
              </td>
            </tr>
          </div>
        </table>
      </q-card>
      <q-space />
      <q-separator />
      <q-space />
      <q-card class="q-pa-md bg-teal-1" style="max-width: 300px">
        <table class="table is-fullwidth">
          <div v-if="Object.keys(selectedFeatureMeanBarBox).length > 0">
            <tr>
              <td>
                <apexchart width="280" type="radialBar" :options="apxmeanoptions" :series="selectedFeatureMeanBarBox" />
              </td>
            </tr>
          </div>
        </table>
      </q-card>
      <q-space />
      <q-separator />
      <q-space />
      <q-card class="q-pa-md bg-teal-1" style="max-width: 300px">
        <table class="table is-fullwidth">
          <div v-if="Object.keys(selectedFeaturePrcastBarBox).length > 0">
            <tr>
              <td>
                <apexchart width="280" type="radialBar" :options="apxprcastoptions" :series="selectedFeaturePrcastBarBox" />
              </td>
            </tr>
          </div>
        </table>
      </q-card>
      <q-space />
      <q-separator />
      <q-space />
      <q-card class="q-pa-md bg-teal-1" style="max-width: 300px">
        <table class="table is-fullwidth">
          <div v-if="Object.keys(selectedFeatureMinBarBox).length > 0">
            <tr>
              <td>
                <apexchart width="280" type="radialBar" :options="apxminoptions" :series="selectedFeatureMinBarBox" />
              </td>
            </tr>
          </div>
        </table>
      </q-card>
      <q-space />
      <q-separator />
      <q-space />
      <q-card class="q-pa-md bg-teal-1" style="max-width: 300px">
        <table class="table is-fullwidth">
          <div v-if="Object.keys(selectedFeatureMaxBarBox).length > 0">
            <tr>
              <td>
                <apexchart width="280" type="radialBar" :options="apxmaxoptions" :series="selectedFeatureMaxBarBox" />
              </td>
            </tr>
          </div>
        </table>
      </q-card>
      <q-space />
      <q-separator />
      <q-space />
      <q-card class="q-pa-md bg-teal-1" style="max-width: 300px">
        <table class="table is-fullwidth">
          <div v-if="Object.keys(selectedFeatureStdBarBox).length > 0">
            <tr>
              <td>
                <apexchart width="280" type="radialBar" :options="apxstdoptions" :series="selectedFeatureStdBarBox" />
              </td>
            </tr>
          </div>
        </table>
      </q-card>
    </q-drawer>
    <!--// Left Drawer Ends -->

    <!--// right side drawer Starts -->
    <q-drawer side="right" v-model="rightDrawerOpen" show-if-above bordered content-class="teal bg-teal-1">
      <q-list bordered class="rounded-borders">
        <!-- // baselayers -->
        <q-expansion-item default-opened expand-separator icon="list" label="Base Layers">
          <div class="q-pa-md" style="min-width: 200px">
            <q-list link>
              <!--//
                Rendering a <label> tag (notice tag="label")
                so QRadios will respond to clicks on QItems to
                change Toggle state.
              -->
              <q-item tag="label" v-ripple>
                <q-item-section avatar>
                  <q-radio v-on:input="showBaseLayer" val="osm" v-model="baselayer" color="teal" />
                </q-item-section>
                <q-item-section>
                  <q-item-label>OpenStreetMap</q-item-label>
                </q-item-section>
              </q-item>

              <q-item tag="label" v-ripple>
                <q-item-section avatar>
                  <q-radio v-on:input="showBaseLayer" val="mapbox" v-model="baselayer" color="teal" />
                </q-item-section>
                <q-item-section>
                  <q-item-label>MapBox Satellite</q-item-label>
                </q-item-section>
              </q-item>
            </q-list>
          </div>
        </q-expansion-item>
        <!-- // baselayers -->

        <!-- // nolayer -->
        <q-expansion-item expand-separator icon="list" label="No Overlay Layer">
          <div class="q-pa-md" style="min-width: 200px">
            <q-list link>
              <q-item tag="label" v-ripple>
                <q-item-section avatar>
                  <q-radio v-on:input="showMapPanelRadioLayer" val="nolayer" v-model="currentvariable" color="teal" />
                </q-item-section>
                <q-item-section>
                  <q-item-label>No Overlay Layer</q-item-label>
                </q-item-section>
              </q-item>
            </q-list>
          </div>
        </q-expansion-item>
        <!-- // nolayer -->

        <!-- // NC wellwise layers -->
        <q-expansion-item default-opened dense dense-toggle expand-separator icon="list" label="NC Well Data Layers, by Census Tracts">
          <div class="q-pa-md q-gutter-y-sm column">
            <q-item dense tag="label" v-ripple>
              <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">Arsenic (ppb and %)</q-tooltip>
              <table cellspacing="0" cellpadding="0" style="width:100%">
                <caption style="text-align:left">Arsenic</caption>
                <tr>
                  <td>Median</td>
                  <td>Mean</td>
                  <td>% Above Standard</td>
                </tr>
                <tr>
                  <td><q-radio v-on:input="showMapPanelRadioLayer" val="ncwellwise_arsenic_med" v-model="currentvariable" color="teal" /></td>
                  <td><q-radio v-on:input="showMapPanelRadioLayer" val="ncwellwise_arsenic_mean" v-model="currentvariable" color="teal" /></td>
                  <td><q-radio v-on:input="showMapPanelRadioLayer" val="ncwellwise_arsenic_prcast" v-model="currentvariable" color="teal" /></td>
                </tr>
              </table>
            </q-item>
            <q-item dense tag="label" v-ripple>
              <!-- // legend -->
              <div class="q-pa-md q-gutter-y-sm column">
                LEGEND
                <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
                  <font size="2" face="Arial" >
                    <q-markup-table dense class="bg-teal-1">
                      <!-- tr>
                        <td id="nested" -->
                          <tr>
                             <td style="text-align:center;" colspan="2">Median (ppb)</td>
                             <td style="text-align:center;" >Mean (ppb)</td>
                             <td style="text-align:center;" >% Above Standard</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="assqu1"></span></td>
                            <td>&gt; 6.83</td>
                            <td>&gt; 8.95</td>
                            <td>&gt; 16.0</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="assqu2"></span></td>
                            <td>&ge; 6.83 &amp; &lt; 10.12</td>
                            <td>&ge; 8.95 &amp; &lt; 14.93</td>
                            <td>&ge; 16.0 &amp; &lt; 32.0</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="assqu3"></span></td>
                            <td>&ge; 10.12 &amp; &lt; 13.42</td>
                            <td>&ge; 14.93 &amp; &lt; 20.92</td>
                            <td>&ge; 32.0 &amp; &lt; 48.0</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="assqu4"></span></td>
                            <td>&ge; 13.42 &amp; &lt; 16.71</td>
                            <td>&ge; 20.92 &amp; &lt; 26.9</td>
                            <td>&ge; 48.0 &amp; &lt; 64.0</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="assqu5"></span></td>
                            <td>&ge; 16.71</td>
                            <td>&ge; 26.9</td>
                            <td>&ge; 64.0</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="squfill"></span></td>
                            <td>Fill -999.99</td>
                          </tr>
                        <!-- /td>
                      </tr -->
                    </q-markup-table>
                  </font>
                </q-popup-proxy>
              </div>
              <!-- // legend -->
            </q-item>

            <q-item dense tag="label" v-ripple>
              <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">Cadmium (ppb and %)</q-tooltip>
              <table cellspacing="0" cellpadding="0" style="width:100%">
                <caption style="text-align:left">Cadmium</caption>
                <tr>
                  <td>Median</td>
                  <td>Mean</td>
                  <td>% Above Standard</td>
                </tr>
                <tr>
                  <td><q-radio v-on:input="showMapPanelRadioLayer" val="ncwellwise_cadmium_med" v-model="currentvariable" color="teal" /></td>
                  <td><q-radio v-on:input="showMapPanelRadioLayer" val="ncwellwise_cadmium_mean" v-model="currentvariable" color="teal" /></td>
                  <td><q-radio v-on:input="showMapPanelRadioLayer" val="ncwellwise_cadmium_prcast" v-model="currentvariable" color="teal" /></td>
                </tr>
              </table>
            </q-item>
            <q-item dense tag="label" v-ripple>
              <!-- // legend -->
              <div class="q-pa-md q-gutter-y-sm column">
                LEGEND
                <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
                  <font size="2" face="Arial" >
                    <q-markup-table dense class="bg-teal-1">
                      <!-- tr>
                        <td id="nested" -->
                          <tr>
                             <td style="text-align:center;" colspan="2">Median (ppb)</td>
                             <td style="text-align:center;" >Mean (ppb)</td>
                             <td style="text-align:center;" >% Above Standard</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="cdsqu1"></span></td>
                            <td>&gt; 0.74</td>
                            <td>&gt; 2.71</td>
                            <td>&gt; 4.0</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="cdsqu2"></span></td>
                            <td>&ge; 0.74 &amp; &lt; 0.77</td>
                            <td>&ge; 2.71 &amp; &lt; 4.72</td>
                            <td>&ge; 4.0 &amp; &lt; 8.0</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="cdsqu3"></span></td>
                            <td>&ge; 0.77 &amp; &lt; 0.79</td>
                            <td>&ge; 4.72 &amp; &lt; 6.72</td>
                            <td>&ge; 8.0 &amp; &lt; 12.0</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="cdsqu4"></span></td>
                            <td>&ge; 0.79 &amp; &lt; 0.82</td>
                            <td>&ge; 6.72 &amp; &lt; 8.73</td>
                            <td>&ge; 12.0 &amp; &lt; 16.0</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="cdsqu5"></span></td>
                            <td>&ge; 0.82</td>
                            <td>&ge; 8.73</td>
                            <td>&ge; 16.0</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="squfill"></span></td>
                            <td>Fill -999.99</td>
                          </tr>
                        <!-- /td>
                      </tr -->
                    </q-markup-table>
                  </font>
                </q-popup-proxy>
              </div>
              <!-- // legend -->
            </q-item>

            <q-item dense tag="label" v-ripple>
              <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">Lead (ppb and %)</q-tooltip>
              <table cellspacing="0" cellpadding="0" style="width:100%">
                <caption style="text-align:left">Lead</caption>
                <tr>
                  <td>Median</td>
                  <td>Mean</td>
                  <td>% Above Standard</td>
                </tr>
                <tr>
                  <td><q-radio v-on:input="showMapPanelRadioLayer" val="ncwellwise_lead_med" v-model="currentvariable" color="teal" /></td>
                  <td><q-radio v-on:input="showMapPanelRadioLayer" val="ncwellwise_lead_mean" v-model="currentvariable" color="teal" /></td>
                  <td><q-radio v-on:input="showMapPanelRadioLayer" val="ncwellwise_lead_prcast" v-model="currentvariable" color="teal" /></td>
                </tr>
              </table>
            </q-item>
            <q-item dense tag="label" v-ripple>
              <!-- // legend -->
              <div class="q-pa-md q-gutter-y-sm column">
                LEGEND
                <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
                  <font size="2" face="Arial" >
                    <q-markup-table dense class="bg-teal-1">
                      <!-- tr>
                        <td id="nested" -->
                          <tr>
                             <td style="text-align:center;" colspan="2">Median (ppb)</td>
                             <td style="text-align:center;" >Mean (ppb)</td>
                             <td style="text-align:center;" >% Above Standard</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="pbsqu1"></span></td>
                            <td>&gt; 11.69</td>
                            <td>&gt; 39.22</td>
                            <td>&gt; 20.0</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="pbsqu2"></span></td>
                            <td>&ge; 11.69 &amp; &lt; 19.83</td>
                            <td>&ge; 39.22 &amp; &lt; 75.53</td>
                            <td>&ge; 20.0 &amp; &lt; 40.0</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="pbsqu3"></span></td>
                            <td>&ge; 19.83 &amp; &lt; 27.98</td>
                            <td>&ge; 75.53 &amp; &lt; 111.83</td>
                            <td>&ge; 40.0 &amp; &lt; 60.0</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="pbsqu4"></span></td>
                            <td>&ge; 27.98 &amp; &lt; 36.12</td>
                            <td>&ge; 111.83 &amp; &lt; 148.14</td>
                            <td>&ge; 60.0 &amp; &lt; 80.0</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="pbsqu5"></span></td>
                            <td>&ge; 36.12</td>
                            <td>&ge; 148.14</td>
                            <td>&ge; 80.0</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="pbsqufill"></span></td>
                            <td>Fill -999.99</td>
                          </tr>
                        <!-- /td>
                      </tr -->
                    </q-markup-table>
                  </font>
                </q-popup-proxy>
              </div>
              <!-- // legend -->
            </q-item>

            <q-item dense ag="label" v-ripple>
              <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">Maganese (ppb and %)</q-tooltip>
              <table cellspacing="0" cellpadding="0" style="width:100%">
                <caption style="text-align:left">Manganese</caption>
                <tr>
                  <td>Median</td>
                  <td>Mean</td>
                  <td>% Above Standard</td>
                </tr>
                <tr>
                  <td><q-radio v-on:input="showMapPanelRadioLayer" val="ncwellwise_manganese_med" v-model="currentvariable" color="teal" /></td>
                  <td><q-radio v-on:input="showMapPanelRadioLayer" val="ncwellwise_manganese_mean" v-model="currentvariable" color="teal" /></td>
                  <td><q-radio v-on:input="showMapPanelRadioLayer" val="ncwellwise_manganese_prcast" v-model="currentvariable" color="teal" /></td>
                </tr>
              </table>
            </q-item>
            <q-item dense tag="label" v-ripple>
              <!-- // legend -->
              <div class="q-pa-md q-gutter-y-sm column">
                LEGEND
                <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
                  <font size="2" face="Arial" >
                    <q-markup-table dense class="bg-teal-1">
                      <!-- tr>
                        <td id="nested" -->
                          <tr>
                             <td style="text-align:center;" colspan="2">Median (ppb)</td>
                             <td style="text-align:center;" >Mean (ppb)</td>
                             <td style="text-align:center;" >% Above Standard</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="mnsqu1"></span></td>
                            <td>&gt; 184.4</td>
                            <td>&gt; 213.09</td>
                            <td>&gt; 20.0</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="mnsqu2"></span></td>
                            <td>&ge; 184.4 &amp; &lt; 350.8</td>
                            <td>&ge; 213.09 &amp; &lt; 404.97</td>
                            <td>&ge; 20.0 &amp; &lt; 40.0</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="mnsqu3"></span></td>
                            <td>&ge; 350.8 &amp; &lt; 517.2</td>
                            <td>&ge; 404.97 &amp; &lt; 596.85</td>
                            <td>&ge; 40.0 &amp; &lt; 60.0</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="mnsqu4"></span></td>
                            <td>&ge; 517.2 &amp; &lt; 683.6</td>
                            <td>&ge; 596.85 &amp; &lt; 788.73</td>
                            <td>&ge; 60.0 &amp; &lt; 80.0</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="mnsqu5"></span></td>
                            <td>&ge; 683.6</td>
                            <td>&ge; 788.73</td>
                            <td>&ge; 80.0</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="squfill"></span></td>
                            <td>Fill -999.99</td>
                          </tr>
                        <!-- /td>
                      </tr -->
                    </q-markup-table>
                  </font>
                </q-popup-proxy>
              </div>
              <!-- // legend -->
            </q-item>
          </div>
        </q-expansion-item>
        <!-- // NC wellwise layers -->

        <!-- // ACS Census layers -->
        <q-expansion-item dense dense-toggle expand-separator icon="list" label="Socioeconomic Layers, by Census Tracts">
          <div class="q-pa-md q-gutter-y-sm column">
            <q-item dense tag="label" v-ripple>
              <!-- // legend -->
              <div class="q-pa-md q-gutter-y-sm column">
                LEGEND
                <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
                  <font size="2" face="Arial" >
                    <q-markup-table dense class="bg-teal-1">
                      <tr>
                        <td style="padding:5px"><span class="acssqu1"></span></td>
                        <td>&gt; 15%</td>
                      </tr>
                      <tr>
                        <td style="padding:5px"><span class="acssqu2"></span></td>
                        <td>&ge; 15% &amp; &lt; 30%</td>
                      </tr>
                      <tr>
                        <td style="padding:5px"><span class="acssqu3"></span></td>
                        <td>&ge; 30% &amp; &lt; 45%</td>
                      </tr>
                      <tr>
                        <td style="padding:5px"><span class="acssqu4"></span></td>
                        <td>&ge; 45% &amp; &lt; 60%</td>
                      </tr>
                      <tr>
                        <td style="padding:5px"><span class="acssqu5"></span></td>
                        <td>&ge; 60% &amp; &lt; 75%</td>
                      </tr>
                      <tr>
                        <td style="padding:5px"><span class="acssqu6"></span></td>
                        <td>&ge; 75%</td>
                      </tr>
                      <tr>
                        <td style="padding:5px"><span class="squfill"></span></td>
                        <td>Fill -999.99</td>
                      </tr>
                    </q-markup-table>
                  </font>
                </q-popup-proxy>
              </div>
              <!-- // legend -->
            </q-item>

            <q-item tag="label" v-ripple>
              <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="percent_below_poverty_level" v-model="currentvariable" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>Percent Below the Poverty Level</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="american_indian_and_alaska_native_alone" v-model="currentvariable" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>Percent Native American</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="asian_alone" v-model="currentvariable" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>Percent Asian</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="black_or_african_american_alone" v-model="currentvariable" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>Percent Non-Hispanic Black</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="native_hawaiian_and_other_pacific_islander_alone" v-model="currentvariable" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>Percent Non-Hispanic Native Hawaiian and other Pacific Islander</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="white_alone" v-model="currentvariable" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>Percent Non-Hispanic White</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="two_or_more_races" v-model="currentvariable" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>Percent Two or more Races</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="hispanic_or_latino_of_any_race" v-model="currentvariable" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>Percent Hispanic</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="not_hispanic_or_latino" v-model="currentvariable" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>Percent Non-Hispanic</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="speak_a_language_other_than_english" v-model="currentvariable" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>Percent of Population, 5 Years and Over, who Speak a language other than English</q-item-label>
              </q-item-section>
            </q-item>
          </div>
        </q-expansion-item>
        <!-- // ACS Census layers -->

        <!-- // EJScreen layers -->
        <q-expansion-item dense dense-toggle expand-separator icon="list" label="Environmental Justice Layers, by Census Block Group">
          <div class="q-pa-md q-gutter-y-sm column">
            <q-item dense tag="label" v-ripple>
              <!-- // legend -->
              <div class="q-pa-md q-gutter-y-sm column">
                LEGEND
                <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
                  <font size="2" face="Arial" >
                    <q-markup-table dense class="bg-teal-1">
                      <!-- tr>
                        <td id="nested" -->
                          <tr>
                             <td style="text-align:center;" colspan="2">Lead Paint</td>
                             <td style="text-align:center;" >Diesel Particulate</td>
                             <td style="text-align:center;" >Air Toxics Cancer</td>
                             <td style="text-align:center;" >Air toxics respiratory</td>
                             <td style="text-align:center;" >Traffic</td>
                             <td style="text-align:center;" >Direct Dischargers</td>
                             <td style="text-align:center;" >National Priorities </td>
                             <td style="text-align:center;" >Risk Management</td>
                             <td style="text-align:center;" >Storage and Disposal</td>
                             <td style="text-align:center;" >Ozone</td>
                             <td style="text-align:center;" >PM2.5</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="ejssqu1"></span></td>
                            <td>&gt;-200.0</td>
                            <td>&gt;-300.0</td>
                            <td>&gt;-45000.0</td>
                            <td>&gt;-600.0</td>
                            <td>&gt;800000.0</td>
                            <td>&gt;-47000.0</td>
                            <td>&gt;-400.0</td>
                            <td>&gt;-450.0</td>
                            <td>&gt;-3200.0</td>
                            <td>&gt;-58000.0</td>
                            <td>&gt;-11000.0</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="ejssqu2"></span></td>
                            <td>&ge; -200.0 &amp; &lt; 0.0</td>
                            <td>&ge; -300.0 &amp; &lt; 0.0</td>
                            <td>&ge; -45000.0 &amp; &lt; -20000.0</td>
                            <td>&ge; -600.0 &amp; &lt; -250</td>
                            <td>&ge; 800000.0 &amp; &lt; 1700000.0</td>
                            <td>&ge; -47000.0 &amp; &lt; -35000.0</td>
                            <td>&ge; -400.0 &amp; &lt; -120.0</td>
                            <td>&ge; -450.0 &amp; &lt; 1000.0</td>
                            <td>&ge; -3200.0 &amp; &lt; -1000.0</td>
                            <td>&ge; -58000.0 &amp; &lt; -28000.0</td>
                            <td>&ge; -11000.0 &amp; &lt; -5500.0</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="ejssqu3"></span></td>
                            <td>&ge; 0.0 &amp; &lt; 200.0</td>
                            <td>&ge; 0.0 &amp; &lt; 280.0</td>
                            <td>&ge; -20000.0 &amp; &lt; 5000.0</td>
                            <td>&ge; -250.0 &amp; &lt; 100.0</td>
                            <td>&ge; 1700000.0 &amp; &lt; 1700000.0</td>
                            <td>&ge; -35000.0 &amp; &lt; -22000.0</td>
                            <td>&ge; -120.0 &amp; &lt; 150.0</td>
                            <td>&ge; 1000.0 &amp; &lt; 2450.0</td>
                            <td>&ge; -1000.0 &amp; &lt; 1800.0</td>
                            <td>&ge; -28000.0 &amp; &lt; 600.0</td>
                            <td>&ge; -5500.0 &amp; &lt; 1000.0</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="ejssqu4"></span></td>
                            <td>&ge; 200.0 &amp; &lt; 400.0</td>
                            <td>&ge; 280.0 &amp; &lt; 580.0</td>
                            <td>&ge; 5000.0 &amp; &lt; 30000.0</td>
                            <td>&ge; 100.0 &amp; &lt; 450.0</td>
                            <td>&ge; 2600000.0 &amp; &lt; 2600000.0</td>
                            <td>&ge; -22000.0 &amp; &lt; -10000.0</td>
                            <td>&ge; 150.0 &amp; &lt; 420.0</td>
                            <td>&ge; 2450.0 &amp; &lt; 3900.0</td>
                            <td>&ge; 1800.0 &amp; &lt; 4600.0</td>
                            <td>&ge; 600.0 &amp; &lt; 38000.0</td>
                            <td>&ge; 1000.0 &amp; &lt; 7500.0</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="ejssqu5"></span></td>
                            <td>&ge; 400.0 &amp; &lt; 600.0</td>
                            <td>&ge; 580.0 &amp; &lt; 850.0</td>
                            <td>&ge; 30000.0 &amp; &lt; 55000.0</td>
                            <td>&ge; 450.0 &amp; &lt; 800.0</td>
                            <td>&ge; 3500000.0 &amp; &lt; 4400000.0</td>
                            <td>&ge; -10000.0 &amp; &lt; 200.0</td>
                            <td>&ge; 420.0 &amp; &lt; 690.0</td>
                            <td>&ge; 3900.0 &amp; &lt; 5350.0</td>
                            <td>&ge; 4600.0 &amp; &lt; 7300.0</td>
                            <td>&ge; 38000.0 &amp; &lt; 70000.0</td>
                            <td>&ge; 7500.0 &amp; &lt; 15000.0</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="ejssqu6"></span></td>
                            <td>&ge; 600.0</td>
                            <td>&ge; 850.0</td>
                            <td>&ge; 55000.0</td>
                            <td>&ge; 800.0</td>
                            <td>&ge; 4400000.0</td>
                            <td>&ge; 200.0</td>
                            <td>&ge; 690.0</td>
                            <td>&ge; 5350.0</td>
                            <td>&ge; 7300.0</td>
                            <td>&ge; 70000.0</td>
                            <td>&ge; 15000.0</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="squfill"></span></td>
                            <td>Fill -999.99</td>
                          </tr>
                        <!-- /td>
                      </tr -->
                    </q-markup-table>
                  </font>
                </q-popup-proxy>
              </div>
              <!-- // legend -->
            </q-item>

            <q-item tag="label" v-ripple>
              <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="d_ldpnt_2" v-model="currentvariable" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>EJ Index for % pre-1960 housing (lead paint indicator)</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="d_dslpm_2" v-model="currentvariable" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>EJ Index for Diesel particulate matter level in air</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="d_cancr_2" v-model="currentvariable" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>EJ Index for Air toxics cancer risk</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="d_resp_2" v-model="currentvariable" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>EJ Index for Air toxics respiratory hazard index</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="d_ptraf_2" v-model="currentvariable" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>EJ Index for Traffic proximity and volume</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="d_pwdis_2" v-model="currentvariable" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>EJ Index for Indicator for major direct dischargers to water</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="d_pnpl_2" v-model="currentvariable" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>EJ Index for Proximity to National Priorities List (NPL) sites</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="d_prmp_2" v-model="currentvariable" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>EJ Index for Proximity to Risk Management Plan (RMP) facilities</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="d_ptsdf_2" v-model="currentvariable" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>EJ Index for Proximity to Treatment Storage and Disposal (TSDF) facilities</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="d_ozone_2" v-model="currentvariable" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>EJ Index for Ozone level in air</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="d_pm25_2" v-model="currentvariable" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>EJ Index for PM2.5 level in air</q-item-label>
              </q-item-section>
            </q-item>
          </div>
        </q-expansion-item>
        <!-- // EJScreen layers -->

        <!-- // Health layers -->
        <q-expansion-item dense dense-toggle expand-separator icon="list" label="Health Layers, by Zip Code">
          <div class="q-pa-md q-gutter-y-sm column">
            <q-item dense tag="label" v-ripple>
              <!-- // legend -->
              <div class="q-pa-md q-gutter-y-sm column">
                LEGEND
                <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
                  <font size="2" face="Arial" >
                    <q-markup-table dense class="bg-teal-1">
                      <!-- tr>
                        <td id="nested" -->
                          <tr>
                             <td style="text-align:center;" colspan="2">Total Cases</td>
                             <td style="text-align:center;" >Cases Per 10,000 Residents</td>
                             <td style="text-align:center;" >Cases Per 100,000 Residents</td>
                             <td style="text-align:center;" >Deaths</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="heasqu1"></span></td>
                            <td>&gt; 1328</td>
                            <td>&gt; 586.0</td>
                            <td>&gt; 5859.0</td>
                            <td>&gt; 17</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="heasqu2"></span></td>
                            <td>&ge; 1328 &amp; &lt; 2656</td>
                            <td>&ge; 586.0 &amp; &lt; 1172.0</td>
                            <td>&ge; 5859.0 &amp; &lt; 11718.0</td>
                            <td>&ge; 17 &amp; &lt; 34</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="heasqu3"></span></td>
                            <td>&ge; 2656 &amp; &lt; 3984</td>
                            <td>&ge; 1172.0 &amp; &lt; 1758.0</td>
                            <td>&ge; 11718.0 &amp; &lt; 17577.0</td>
                            <td>&ge; 34 &amp; &lt; 51</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="heasqu4"></span></td>
                            <td>&ge; 3984 &amp; &lt; 5416</td>
                            <td>&ge; 1758.0 &amp; &lt; 2344.0</td>
                            <td>&ge; 17577.0 &amp; &lt; 23436.0</td>
                            <td>&ge; 51 &amp; &lt; 65</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="heasqu5"></span></td>
                            <td>&ge; 5416 &amp; &lt; 6644</td>
                            <td>&ge; 2344.0 &amp; &lt; 2930.0</td>
                            <td>&ge; 23436.0 &amp; &lt; 29295.0</td>
                            <td>&ge; 65 &amp; &lt; 85</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="heasqu6"></span></td>
                              <td>&ge; 6644</td>
                              <td>&ge; 2930.0
                              <td>&ge; 29295.0</td>
                              <td>&ge; 85</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="squfill"></span></td>
                            <td>Fill -999.99</td>
                          </tr>
                        <!-- /td>
                      </tr -->
                    </q-markup-table>
                  </font>
                </q-popup-proxy>
              </div>
              <!-- // legend -->
            </q-item>

            <q-item tag="label" v-ripple>
              <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From North Carolina Department of Health and Human Services</q-tooltip>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="cases" v-model="currentvariable" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>Covid-19 Total Cases</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From North Carolina Department of Health and Human Services</q-tooltip>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="cases_per_10000_res" v-model="currentvariable" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>Covid-19 Cases Per 10,000 Residents</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From North Carolina Department of Health and Human Services</q-tooltip>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="cases_per_100000_res" v-model="currentvariable" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>Covid-19 Cases Per 100,000 Residents-</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From North Carolina Department of Health and Human Services</q-tooltip>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="deaths" v-model="currentvariable" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>Covid-19 Deaths</q-item-label>
              </q-item-section>
            </q-item>
           </div>
        </q-expansion-item>
        <!-- // Health layers -->

        <!-- // Ancillary layers -->
        <q-expansion-item dense dense-toggle expand-separator icon="list" label="Ancillary Layers">
          <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From North Carolina One Map</q-tooltip>
          <div class="q-pa-md q-gutter-y-sm column">
            <q-toggle
              :label="`North Carolina Counties ${ ncCountiesModel }`"
              :key="layers[4].id"
              v-on:input="showMapPanelToggleLayer(layers)"
              :class="{ 'is-active': layers[4].visible }"
              color="teal"
              false-value="Not Selected"
              true-value="Selected"
              v-model="ncCountiesModel"
            />
          </div>
        </q-expansion-item>
        <!-- // Ancilary layers -->

        <!-- // state -->
        <q-expansion-item dense dense-toggle expand-separator icon="list" label="State">
          <q-markup-table class="table is-fullwidth bg-teal-1" dense>
            <tr>
              <th class="text-left">Map center</th>
              <td class="text-left" style="font-size:10px">{{ center[0]}}, {{ center[1] }}</td>
            </tr>
            <tr>
              <th class="text-left">Map zoom</th>
              <td class="text-left" style="font-size:10px">{{ zoom }}</td>
            </tr>
            <tr>
              <th class="text-left">Map rotation</th>
              <td class="text-left" style="font-size:10px">{{ rotation }}</td>
            </tr>
            <tr>
              <th class="text-left">Event coordinate</th>
              <td class="text-left" style="font-size:10px">{{ eventCoordinate[0] }}, {{ eventCoordinate[1] }}</td>
            </tr>
            <tr>
              <th class="text-left">Device coordinate</th>
              <td class="text-left" style="font-size:10px">{{ deviceCoordinate[0] }}, {{ deviceCoordinate[1] }}</td>
            </tr>
            <tr>
              <th class="text-left">Coordinate accuracy</th>
              <td class="text-left" style="font-size:10px">{{ coordinateAccuracy }} meters</td>
            </tr>
            <tr>
              <th class="text-left">Selected features</th>
              <td class="text-left" style="font-size:10px">{{ pid }}</td>
            </tr>
          </q-markup-table>
        </q-expansion-item>
        <!-- // state -->

      </q-list>
    </q-drawer>
    <!--// left side drawer Ends -->

    <!--// app map -->
    <vl-map v-if="mapVisible" class="map" ref="map" :load-tiles-while-animating="true" :load-tiles-while-interacting="true"
      @singleclick="onMapClick" data-projection="EPSG:4326" :default-controls="defaultControls" @mounted="onMapMounted"
      :controls="false" style="height:1200px">
       <!--// map view aka ol.View -->
      <vl-view ref="view" :center.sync="center" :zoom.sync="zoom" :rotation.sync="rotation"></vl-view>

      <!--// click interactions -->
      <!-- vl-interaction-select ref="selectInteraction" :layers="layer => !(layer instanceof VectorTile)" :features.sync="selectedFeature" -->
      <!-- vl-interaction-select ref="selectInteraction" :filter="(feature, layer) => feature instanceof Feature" :features.sync="selectedFeature" -->
      <!-- vl-interaction-select ref="selectInteraction" :features.sync="selectedFeature" -->
        <!-- template slot-scope="select" -->
          <!--// select styles -->
          <!-- vl-style-box>
            <vl-style-stroke color="#33201e" :width="7"></vl-style-stroke>
            <vl-style-fill :color="[254, 178, 76, 0.7]"></vl-style-fill>
            <vl-style-circle :radius="5">
              <vl-style-stroke color="#9e493e" :width="7"></vl-style-stroke>
              <vl-style-fill :color="[254, 178, 76, 0.7]"></vl-style-fill>
            </vl-style-circle>
          </vl-style-box>
          <vl-style-box :z-index="1">
            <vl-style-stroke color="#d43f45" :width="2"></vl-style-stroke>
            <vl-style-circle :radius="5">
              <vl-style-stroke color="#d43f45" :width="2"></vl-style-stroke>
            </vl-style-circle>
          </vl-style-box -->
          <!--// select styles -->

          <!--// selected feature popup -->
          <!-- vl-overlay class="feature-popup" v-for="feature in select.features" :key="feature.id" :id="feature.id"
            :position="pointOnSurface(feature.geometry)" :auto-pan="true" :auto-pan-animation="{ duration: 300 }">
            <q-card class="feature-popup">
              <q-card-section>
                <q-banner inline-actions class="text-black bg-white">
                  <div class="text-h6">
                    Feature GeoID {{ feature.properties['geoid10'] }}
                  </div>
                  <template v-slot:action>
                    <q-btn flat round dense icon="close" @click="selectedFeature = selectedFeature.filter(f => f.id !== feature.id)" />
                  </template>
                </q-banner>
                <table class="table is-fullwidth">
                  <div v-if="Object.keys(selectedFeatureMaxBarBox).length > 0">
                  <tr>
                    <td>
                      <apexchart width="400" type="radialBar" :options="apxmeanoptions" :series="selectedFeatureMeanBarBox" />
                    </td>
                  </tr>
                  <tr>
                    <td>
                      <apexchart type="radialBar" :options="apxmeanoptions" :series="selectedFeatureMeanBarBox" />
                    </td>
                  </tr>
                  </div>
                </table>
              </q-card-section>
            </q-card>
          </vl-overlay -->
          <!--// selected feature popup -->
        <!-- /template -->
      <!-- /vl-interaction-select -->
      <!--// click interactions -->

      <!-- geolocation -->
      <div v-if="currentlocation === 'True'">
        <vl-geoloc ref="geoloc" @update:position="onUpdatePosition" enableHighAccuracy="true" maximumAge="0" timeout="Infinity" >
          <template slot-scope="geoloc">
            <vl-feature v-if="geoloc.position" id="position-feature" ref="position">
              <vl-geom-point :coordinates="geoloc.position"></vl-geom-point>
              <vl-style-box>
                <vl-style-icon src="statics/marker.png" :scale="0.4" :anchor="[0.5, 1]" :size="[128, 128]"></vl-style-icon>
              </vl-style-box>
            </vl-feature>
          </template>
        </vl-geoloc>
      </div>
      <!--// geolocation -->

      <!-- address location marker -->
      <div v-if="addresslocation === 'True'">
        <vl-feature id="marker" ref="marker" :properties="{ start: Date.now(), duration: 2500 }">
          <template slot-scope="feature">
            <vl-geom-point :coordinates="addressloc"></vl-geom-point>
            <vl-style-box>
              <vl-style-icon src="statics/marker.png" :scale="0.5" :anchor="[0.5, 1]" :size="[128, 128]"></vl-style-icon>
            </vl-style-box>
            <!-- overlay binded to feature -->
            <vl-overlay v-if="feature.geometry" :position="pointOnSurface(feature.geometry)" :offset="[0, 0]">
            </vl-overlay>
          </template>
        </vl-feature>
      </div>
      <!--// address location marker -->

      <!--// base layers -->
      <vl-layer-tile v-for="layer in baseLayers" :key="layer.name" :id="layer.name" :visible="layer.visible">
        <component :is="'vl-source-' + layer.name" v-bind="layer"></component>
      </vl-layer-tile>
      <!--// base layers -->
      <!-- vl-layer-vector-tile ref="layerSource" :declutter="true">
        <vl-source-vector-tile :url="vtUrl"></vl-source-vector-tile -->
        <!-- vl-source-vector-tile :format-factory="createMvtFormat" :url="vtUrl"></vl-source-vector-tile -->
        <!-- vl-source-vector-tile :format-factory="vtFormatFactory" :url="vtUrl"></vl-source-vector-tile -->
        <!-- vl-style-func ref="layerStyle" :factory="getncwellwiseStyle"></vl-style-func>
      </vl-layer-vector-tile -->
      <!--// other layers from config -->
      <!-- eslint-disable vue/no-use-v-if-with-v-for,vue/no-confusing-v-for-v-if -->
      <vl-layer-vector-tile v-for="layer in layers" :is="layer.cmp" v-if="layer.visible" :key="layer.id" v-bind="layer">
        <component ref="layerSource" :is="layer.source.cmp" v-bind="layer.source" />
        <!-- component ref="layerSource" :is="layer.source.cmp" v-bind="layer.source" :format-factory="createMvtFormat" / -->
        <component ref="layerStyle" v-if="layer.style" v-for="(style, i) in layer.style" :key="i" :is="style.cmp" v-bind="style" />
      </vl-layer-vector-tile>
      <!-- eslint-enable vue/no-use-v-if-with-v-for,vue/no-confusing-v-for-v-if -->
    </vl-map>
    <!--// app map -->

    <!--// left side drawer buttons -->
      <q-page-sticky position="top-left" :offset="[58, 18]">
        <q-btn flat dense round icon="fas fa-sign-out-alt" class="bg-teal text-black" aria-label="Dual Screen Map" @click="$router.replace('/dual')">
          <q-tooltip>Go to Side by Side Screen Map</q-tooltip>
        </q-btn>
      </q-page-sticky>
      <q-page-sticky position="top-left" :offset="[18, 18]">
        <q-btn flat dense round icon="menu" class="bg-teal text-black" @click="leftDrawerOpen = !leftDrawerOpen" aria-label="Menu">
          <q-tooltip>Open &amp; Close Side Drawer</q-tooltip>
        </q-btn>
      </q-page-sticky>
    <!--// left side drawer buttons -->

    <!--// ol map controls -->
    <q-page-sticky position="top-left" :offset="[18, 58]">
      <div id="ZoomTarget"></div>
    </q-page-sticky>
    <q-page-sticky position="bottom-left" :offset="[8, 38]">
      <div id="OverviewMapTarget"></div>
    </q-page-sticky>
    <q-page-sticky position="bottom-left" :offset="[15, 8]">
      <div id="ScaleTarget"></div>
    </q-page-sticky>
    <!--// ol map controls -->

    <!--// right side drawer button -->
    <q-page-sticky position="top-right" :offset="[18, 18]">
      <q-btn flat dense round icon="menu" class="bg-teal text-black" @click="rightDrawerOpen = !rightDrawerOpen" aria-label="Menu">
        <q-tooltip>Open &amp; Close Side Drawer</q-tooltip>
      </q-btn>
    </q-page-sticky>
    <!--// right side drawer button -->

    <!--// full screen button -->
    <q-page-sticky position="top-right" :offset="[18, 58]">
      <q-btn color="teal" class="text-black" @click="$q.fullscreen.toggle()" round :icon="$q.fullscreen.isActive ? 'fullscreen_exit' : 'fullscreen'">
        <q-tooltip>Open &amp; Close Full Screen</q-tooltip>
      </q-btn>
    </q-page-sticky>
    <!--// full screen button -->

    <!--// NC Enviroscan Icon -->
    <q-page-sticky position="top-right" :offset="[98, 5]">
      <q-avatar square size="110px">
        <img src="statics/nc-enviroscan-110.png">
      </q-avatar>
    </q-page-sticky>
    <!--// NC Enviroscan Icon -->

    <!--// select location tools -->
    <q-page-sticky position="bottom-right" :offset="[18, 18]">
      <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">Geolocation Tools</q-tooltip>
      <q-fab icon="keyboard_arrow_up" direction="up" label-position="left" external-label color="teal text-black" label="Geolocation Tools">
        <q-fab-action color="teal" class="text-black" icon="fas fa-map-marked-alt" label-position="left" external-label label="Change Map Location with Address">
          <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
            <q-card class="bg-teal-1">
              <q-banner inline-actions class="bg-teal-1">
                <div class="q-pa-md" style="max-width: 400px">
                  <q-form @submit="address2Geoloc" @reset="resetAddress" class="q-gutter-md">
                    <q-input filled v-model="address" label="Address *" hint="Address, City, State and Country" lazy-rules
                      :rules="[ val => val && val.length > 0 || 'Please type something']"
                    ></q-input>
                    <div>
                      <q-btn label="Submit" type="submit" color="teal"></q-btn>
                      <q-btn label="Reset" type="reset" color="teal" flat class="q-ml-sm"></q-btn>
                    </div>
                  </q-form>
                </div>
                <template align="right" v-slot:action>
                  <q-btn flat round dense icon="close" color="teal" v-close-popup />
                </template>
              </q-banner>
              <q-separator />
            </q-card>
          </q-popup-proxy>
        </q-fab-action>
        <q-fab-action color="teal" class="text-black" icon="fas fa-map-marked-alt" label-position="left" external-label label="Set Map to Current Location">
          <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
            <q-card class="bg-teal-1">
              <q-banner inline-actions class="bg-teal-1">
                <div class="q-pa-md" style="max-width: 400px">
                  <b>Set map to your current location?</b>
                  <div>
                    <q-tabs v-model="getlocation" v-on:input="getCurrentLocation()" no-caps class="bg-teal text-black">
                      <q-tab name="False" label="No" />
                      <q-tab name="True" label="Yes" />
                    </q-tabs>
                  </div>
                </div>
                <template align="right" v-slot:action>
                  <q-btn flat round dense icon="close" color="teal" v-close-popup />
                </template>
              </q-banner>
              <q-separator />
            </q-card>
          </q-popup-proxy>
        </q-fab-action>
      </q-fab>
    </q-page-sticky>
    <!--// select location tools -->

    <!--// base layer map attribution -->
    <q-page-sticky position="bottom-left" :offset="[200, 38]">
      <div id="AttributionTarget"></div>
    </q-page-sticky>
    <!--// base layer map attribution -->
    <q-footer elevated class="bg-teal-1">
      <q-toolbar>
        <div class="text-black">Built With:
          <a href="https://vuejs.org/" target="_blank">Vue</a> /
          <a href="https://quasar.dev/" target="_blank">Quasar</a> /
          <a href="https://vuelayers.github.io/#/" target="_blank">VueLayers</a> /
          <a href="https://openlayers.org/" target="_blank">OpenLayers</a> /
          <a href="https://apexcharts.com/" target="_blank">ApexCharts</a> /
          <a href="https://www.postgresql.org/" target="_blank">Postgres</a> /
          <a href="https://postgis.net/" target="_blank">PostGIS</a> /
          <a href="https://www.djangoproject.com/" target="_blank">Django</a> /
          <a href="https://www.django-rest-framework.org/" target="_blank">Django Rest Framework (DRF)</a> /
          <a href="https://github.com/openwisp/django-rest-framework-gis" target="_blank">DRF-GIS</a> /
          <a href="https://github.com/corteva/djangorestframework-mvt" target="_blank">DRF-MVT</a>
        </div>
      </q-toolbar>
    </q-footer>
  </q-layout>
</template>

<script>
// quasar and vuelayers import
import { openURL } from 'quasar'
import { findPointOnSurface, createStyle } from 'vuelayers/lib/ol-ext'
import { camelCase } from 'lodash'

// ol controls import
import ScaleLine from 'ol/control/ScaleLine'
import OverviewMap from 'ol/control/OverviewMap'
import Zoom from 'ol/control/Zoom'
import Attribution from 'ol/control/Attribution'

// Other ol imports
// import VectorTile from 'ol/layer/VectorTile'
// import Feature from 'ol/Feature'
// import MVT from 'ol/format/MVT'
import { Style, Stroke, Fill } from 'ol/style'

// geocoder
const Nominatim = require('nominatim-geocoder')
const geocoder = new Nominatim({ delay: 1000, secure: true, host: 'nominatim.openstreetmap.org' })

// pubhost and secrets import
import pubhost from '../assets/pubhost.json'
import secrets from '../assets/secrets.json'

let gettoken = function () {
  return secrets[0].MB_KEY
}

export default {
  name: 'NC-Enviroscan',
  components: {
  },
  props: {
    varid: {
      type: String,
      default: ''
    }
  },
  data () {
    return {
      apxmedoptions: {
        colors: ['#a534eb', '#eba234', '#747982', '#19800b'],
        animations: {
          enabled: true,
          easing: 'easeinout',
          speed: 1000
        },
        fill: {
          type: 'gradient',
          gradient: {
            shade: 'dark',
            type: 'vertical',
            shadeIntensity: 0.05,
            inverseColors: false,
            opacityFrom: 1,
            opacityTo: 0.9,
            stops: [0, 100]
          }
        },
        chart: {
          toolbar: {
            show: true
          }
        },
        title: {
          text: 'Median Values',
          align: 'left',
          style: {
            color: '#000'
          }
        },
        plotOptions: {
          radialBar: {
            offsetY: 0,
            offsetX: 0,
            startAngle: 0,
            endAngle: 250,
            hollow: {
              margin: 0,
              size: '25%',
              background: 'transparent',
              image: undefined
            },
            dataLabels: {
              name: {
                show: false

              },
              value: {
                show: false
              }
            }
          }
        },
        labels: ['Arsenic', 'Cadmium', 'Lead', 'Manganese'],
        legend: {
          show: true,
          floating: true,
          fontSize: '12px',
          position: 'left',
          offsetX: -20,
          offsetY: 15,
          labels: {
            useSeriesColors: true
          },
          markers: {
            size: 0
          },
          formatter: function (seriesName, opts) {
            return seriesName + ':  ' + opts.w.globals.series[opts.seriesIndex] + ' ppb'
          },
          itemMargin: {
            horizontal: 1
          }
        },
        responsive: [{
          breakpoint: 480,
          options: {
            legend: {
              show: false
            }
          }
        }]
      },
      apxmeanoptions: {
        colors: ['#a534eb', '#eba234', '#747982', '#19800b'],
        animations: {
          enabled: true,
          easing: 'easeinout',
          speed: 1000
        },
        fill: {
          type: 'gradient',
          gradient: {
            shade: 'dark',
            type: 'vertical',
            shadeIntensity: 0.05,
            inverseColors: false,
            opacityFrom: 1,
            opacityTo: 0.9,
            stops: [0, 100]
          }
        },
        chart: {
          toolbar: {
            show: true
          }
        },
        title: {
          text: 'Mean Values',
          align: 'left',
          style: {
            color: '#000'
          }
        },
        plotOptions: {
          radialBar: {
            offsetY: 0,
            offsetX: 0,
            startAngle: 0,
            endAngle: 250,
            hollow: {
              margin: 0,
              size: '25%',
              background: 'transparent',
              image: undefined
            },
            dataLabels: {
              name: {
                show: false

              },
              value: {
                show: false
              }
            }
          }
        },
        labels: ['Arsenic', 'Cadmium', 'Lead', 'Manganese'],
        legend: {
          show: true,
          floating: true,
          fontSize: '12px',
          position: 'left',
          offsetX: -20,
          offsetY: 15,
          labels: {
            useSeriesColors: true
          },
          markers: {
            size: 0
          },
          formatter: function (seriesName, opts) {
            return seriesName + ':  ' + opts.w.globals.series[opts.seriesIndex] + ' ppb'
          },
          itemMargin: {
            horizontal: 1
          }
        },
        responsive: [{
          breakpoint: 480,
          options: {
            legend: {
              show: false
            }
          }
        }]
      },
      apxprcastoptions: {
        colors: ['#a534eb', '#eba234', '#747982', '#19800b'],
        animations: {
          enabled: true,
          easing: 'easeinout',
          speed: 1000
        },
        fill: {
          type: 'gradient',
          gradient: {
            shade: 'dark',
            type: 'vertical',
            shadeIntensity: 0.05,
            inverseColors: false,
            opacityFrom: 1,
            opacityTo: 0.9,
            stops: [0, 100]
          }
        },
        chart: {
          toolbar: {
            show: true
          }
        },
        title: {
          text: '% Above Standard Value',
          align: 'left',
          style: {
            color: '#000'
          }
        },
        plotOptions: {
          radialBar: {
            offsetY: 0,
            offsetX: 0,
            startAngle: 0,
            endAngle: 250,
            hollow: {
              margin: 0,
              size: '25%',
              background: 'transparent',
              image: undefined
            },
            dataLabels: {
              name: {
                show: false

              },
              value: {
                show: false
              }
            }
          }
        },
        labels: ['Arsenic', 'Cadmium', 'Lead', 'Manganese'],
        legend: {
          show: true,
          floating: true,
          fontSize: '12px',
          position: 'left',
          offsetX: -20,
          offsetY: 15,
          labels: {
            useSeriesColors: true
          },
          markers: {
            size: 0
          },
          formatter: function (seriesName, opts) {
            return seriesName + ':  ' + opts.w.globals.series[opts.seriesIndex] + ' %'
          },
          itemMargin: {
            horizontal: 1
          }
        },
        responsive: [{
          breakpoint: 480,
          options: {
            legend: {
              show: false
            }
          }
        }]
      },
      apxminoptions: {
        colors: ['#a534eb', '#eba234', '#747982', '#19800b'],
        animations: {
          enabled: true,
          easing: 'easeinout',
          speed: 1000
        },
        fill: {
          type: 'gradient',
          gradient: {
            shade: 'dark',
            type: 'vertical',
            shadeIntensity: 0.05,
            inverseColors: false,
            opacityFrom: 1,
            opacityTo: 0.9,
            stops: [0, 100]
          }
        },
        chart: {
          toolbar: {
            show: true
          }
        },
        title: {
          text: 'Minimum Values',
          align: 'left',
          style: {
            color: '#000'
          }
        },
        plotOptions: {
          radialBar: {
            offsetY: 0,
            offsetX: 0,
            startAngle: 0,
            endAngle: 250,
            hollow: {
              margin: 0,
              size: '25%',
              background: 'transparent',
              image: undefined
            },
            dataLabels: {
              name: {
                show: false

              },
              value: {
                show: false
              }
            }
          }
        },
        labels: ['Arsenic', 'Cadmium', 'Lead', 'Manganese'],
        legend: {
          show: true,
          floating: true,
          fontSize: '12px',
          position: 'left',
          offsetX: -20,
          offsetY: 15,
          labels: {
            useSeriesColors: true
          },
          markers: {
            size: 0
          },
          formatter: function (seriesName, opts) {
            return seriesName + ':  ' + opts.w.globals.series[opts.seriesIndex] + ' ppb'
          },
          itemMargin: {
            horizontal: 1
          }
        },
        responsive: [{
          breakpoint: 480,
          options: {
            legend: {
              show: false
            }
          }
        }]
      },
      apxmaxoptions: {
        colors: ['#a534eb', '#eba234', '#747982', '#19800b'],
        animations: {
          enabled: true,
          easing: 'easeinout',
          speed: 1000
        },
        fill: {
          type: 'gradient',
          gradient: {
            shade: 'dark',
            type: 'vertical',
            shadeIntensity: 0.05,
            inverseColors: false,
            opacityFrom: 1,
            opacityTo: 0.9,
            stops: [0, 100]
          }
        },
        chart: {
          toolbar: {
            show: true
          }
        },
        title: {
          text: 'Maximum Values',
          align: 'left',
          style: {
            color: '#000'
          }
        },
        plotOptions: {
          radialBar: {
            offsetY: -10,
            offsetX: 0,
            startAngle: 0,
            endAngle: 250,
            hollow: {
              margin: 5,
              size: '30%',
              background: 'transparent',
              image: undefined
            },
            dataLabels: {
              name: {
                show: false

              },
              value: {
                show: false
              }
            }
          }
        },
        labels: ['Arsenic', 'Cadmium', 'Lead', 'Manganese'],
        legend: {
          show: true,
          floating: true,
          fontSize: '12px',
          position: 'left',
          offsetX: -20,
          offsetY: 20,
          labels: {
            useSeriesColors: true
          },
          markers: {
            size: 0
          },
          formatter: function (seriesName, opts) {
            return seriesName + ':  ' + opts.w.globals.series[opts.seriesIndex] + ' ppb'
          },
          itemMargin: {
            horizontal: 1
          }
        },
        responsive: [{
          breakpoint: 480,
          options: {
            legend: {
              show: false
            }
          }
        }]
      },
      apxstdoptions: {
        colors: ['#a534eb', '#eba234', '#747982', '#19800b'],
        animations: {
          enabled: true,
          easing: 'easeinout',
          speed: 1000
        },
        fill: {
          type: 'gradient',
          gradient: {
            shade: 'dark',
            type: 'vertical',
            shadeIntensity: 0.05,
            inverseColors: false,
            opacityFrom: 1,
            opacityTo: 0.9,
            stops: [0, 100]
          }
        },
        chart: {
          toolbar: {
            show: true
          }
        },
        title: {
          text: 'Standard Deviation Values',
          align: 'left',
          style: {
            color: '#000'
          }
        },
        plotOptions: {
          radialBar: {
            offsetY: 0,
            offsetX: 0,
            startAngle: 0,
            endAngle: 250,
            hollow: {
              margin: 0,
              size: '25%',
              background: 'transparent',
              image: undefined
            },
            dataLabels: {
              name: {
                show: false

              },
              value: {
                show: false
              }
            }
          }
        },
        labels: ['Arsenic', 'Cadmium', 'Lead', 'Manganese'],
        legend: {
          show: true,
          floating: true,
          fontSize: '12px',
          position: 'left',
          offsetX: -20,
          offsetY: 15,
          labels: {
            useSeriesColors: true
          },
          markers: {
            size: 0
          },
          formatter: function (seriesName, opts) {
            return seriesName + ':  ' + opts.w.globals.series[opts.seriesIndex] + ' ppb'
          },
          itemMargin: {
            horizontal: 1
          }
        },
        responsive: [{
          breakpoint: 480,
          options: {
            legend: {
              show: false
            }
          }
        }]
      },
      // map parameters
      defaultControls: {
        attribution: true,
        rotate: false,
        zoom: false
      },
      center: [-79.0193, 35.0],
      getlocation: 'False',
      currentlocation: 'False',
      addresslocation: 'False',
      addressloc: [NaN, NaN],
      // center: [NaN, NaN],
      zoom: 8,
      rotation: 0,
      mapVisible: true,
      leftDrawerOpen: false,
      rightDrawerOpen: false,
      longitude: null,
      latitude: null,
      pid: undefined,
      // variable colors
      varcolor: null,
      arsncolors: ['rgba(91, 95, 99, 0.65)', 'rgba(235, 52, 220, 0.65)', 'rgba(186, 52, 235, 0.65)', 'rgba(165, 52, 235, 0.65)',
        'rgba(143, 52, 235, 0.65)', 'rgba(119, 52, 235, 0.65)'],
      cadmcolors: ['rgba(91, 95, 99, 0.65)', 'rgba(223, 235, 52, 0.65)', 'rgba(235, 192, 52, 0.65)', 'rgba(235, 162, 52, 0.65)',
        'rgba(235, 131, 52, 0.65)', 'rgba(235, 89, 52, 0.65)'],
      leadcolors: ['rgba(50, 110, 219, 0.65)', 'rgba(196, 200, 207, 0.65)', 'rgba(156, 162, 173, 0.65)', 'rgba(116, 121, 130, 0.65)',
        'rgba(79, 82, 89, 0.65)', 'rgba(39, 40, 43, 0.65)'],
      mngncolors: ['rgba(91, 95, 99, 0.65)', 'rgba(194, 232, 190, 0.65)', 'rgba(81, 222, 67, 0.65)', 'rgba(25, 128, 11, 0.65)',
        'rgba(14, 82, 5, 0.65)', 'rgba(5, 97, 76, 0.65)'],
      acscolors: ['rgba(91, 95, 99, 0.65)', 'rgba(252, 210, 211, 0.65)', 'rgba(252, 109, 114, 0.65)', 'rgba(247, 59, 66, 0.65)',
        'rgba(250, 2, 11, 0.65)', 'rgba(181, 2, 6, 0.65)', 'rgba(140, 1, 5, 0.65)'],
      ejscolors: ['rgba(91, 95, 99, 0.65)', 'rgba(235, 252, 3, 0.65)', 'rgba(252, 227, 3, 0.65)', 'rgba(252, 186, 3, 0.65)',
        'rgba(252, 128, 3, 0.65)', 'rgba(252, 82, 3, 0.65)', 'rgba(140, 1, 5, 0.65)'],
      covidcolors: ['rgba(91, 95, 99, 0.65)', 'rgba(34, 240, 219, 0.65)', 'rgba(34, 223, 240, 0.65)', 'rgba(34, 185, 240, 0.65)',
        'rgba(22, 141, 245, 0.65)', 'rgba(22, 74, 245, 0.65)', 'rgba(23, 2, 247, 0.65)'],
      // ncwellwise features
      selectedFeature: [],
      selectedFeatureMeanBarBox: [],
      selectedFeatureMedBarBox: [],
      selectedFeaturePrcastBarBox: [],
      selectedFeatureMinBarBox: [],
      selectedFeatureMaxBarBox: [],
      selectedFeatureStdBarBox: [],
      // Other layers attributes
      ncCountiesModel: 'Not Selected',
      address: null,
      acceptaddress: false,
      vtSelection: {},
      vtIdProp: 'geoid10',
      // state attributes
      eventCoordinate: [NaN, NaN],
      deviceCoordinate: [NaN, NaN],
      coordinateAccuracy: undefined,
      // baselayers config
      baselayer: 'osm',
      baseLayers: [
        {
          name: 'osm',
          title: 'OpenStreetMap',
          visible: true
        },
        {
          name: 'mapbox',
          title: 'Mapbox Satellite',
          // mapId: 'mapbox.mapbox-streets-v7',
          mapId: 'mapbox.satellite',
          accessToken: gettoken(),
          visible: false
        }
      ],
      // layers config
      currentvariable: 'ncwellwise_arsenic_med',
      // vtUrl: 'http://' + pubhost[0].PUBHOST_URL + '/drf/apimvt/v1/data/ncwellwise_subset_20102019_geom.mvt?tile={z}/{x}/{y}',
      layers: [
        {
          id: this.getNCWellwiseLayerID(),
          title: 'NC Wellwise',
          // cmp: 'vl-layer-vector',
          cmp: 'vl-layer-vector-tile',
          visible: true,
          source: {
            // cmp: 'vl-source-vector',
            cmp: 'vl-source-vector-tile',
            // url: 'http://' + pubhost[0].PUBHOST_URL + '/drf/api/ncwellwise_subset_20102019_geom/?format=json'
            url: 'http://' + pubhost[0].PUBHOST_URL + '/drf/apimvt/v1/data/ncwellwise_subset_20102019_geom.mvt?tile={z}/{x}/{y}'
          },
          style: [
            {
              cmp: 'vl-style-func',
              factory: this.getncwellwiseStyle
            }
          ]
        },
        {
          id: this.getACSCensusLayerID(),
          title: 'ACS Census',
          cmp: 'vl-layer-vector-tile',
          visible: false,
          source: {
            cmp: 'vl-source-vector-tile',
            url: 'http://' + pubhost[0].PUBHOST_URL + '/drf/apimvt/v1/data/acs_2019_5y_estimates_geom.mvt?tile={z}/{x}/{y}'
          },
          style: [
            {
              cmp: 'vl-style-func',
              factory: this.getacsStyle
            }
          ]
        },
        {
          id: this.getEJScreenLayerID(),
          title: 'EJScreen',
          cmp: 'vl-layer-vector-tile',
          visible: false,
          source: {
            cmp: 'vl-source-vector-tile',
            url: 'http://' + pubhost[0].PUBHOST_URL + '/drf/apimvt/v1/data/ejscreen_subset_geom.mvt?tile={z}/{x}/{y}'
          },
          style: [
            {
              cmp: 'vl-style-func',
              factory: this.getejscreenStyle
            }
          ]
        },
        {
          id: this.getCovid19LayerID(),
          title: 'Covid19',
          cmp: 'vl-layer-vector-tile',
          visible: false,
          source: {
            cmp: 'vl-source-vector-tile',
            url: 'http://' + pubhost[0].PUBHOST_URL + '/drf/apimvt/v1/data/nc_covid_zipcode_geom.mvt?tile={z}/{x}/{y}'
          },
          style: [
            {
              cmp: 'vl-style-func',
              factory: this.getcovid19Style
            }
          ]
        },
        {
          id: 'ncCounties',
          title: 'NC Counties',
          cmp: 'vl-layer-vector-tile',
          visible: false,
          source: {
            cmp: 'vl-source-vector-tile',
            url: 'http://' + pubhost[0].PUBHOST_URL + '/drf/apimvt/v1/data/ncdot_county_boundaries.mvt?tile={z}/{x}/{y}'
          },
          style: [
            {
              cmp: 'vl-style-func',
              factory: this.getNCCountiesStyle
            }
          ]
        },
        {
          id: 'noLayer',
          title: 'No Layer',
          cmp: 'vl-layer-vector-tile',
          visible: false,
          source: {
            cmp: 'vl-source-vector-tile',
            url: 'http://' + pubhost[0].PUBHOST_URL + '/drf/apimvt/v1/data/ncdot_county_boundaries.mvt?tile={z}/{x}/{y}'
          },
          style: [
            {
              cmp: 'vl-style-func',
              factory: this.getNoLayerStyle
            }
          ]
        }
      ]
    }
  },
  created: function () {
    // get current location, and use it for map center
    /* this.$getLocation()
      .then(coordinates => {
        this.center = [coordinates.lng, coordinates.lat]
      }) */
  },
  methods: {
    openURL,
    camelCase,
    pointOnSurface: findPointOnSurface,
    // VectorTile,
    /* Feature,
    createMvtFormat () {
      return new MVT({
        featureClass: Feature
      })
    },
    vtFormatFactory () {
      return new MVT()
    }, */
    getCurrentLocation () {
      if (this.getlocation === 'True') {
        this.addresslocation = 'False'
        this.currentlocation = 'True'
      } else if (this.getlocation === 'False') {
        this.currentlocation = 'False'
      }
    },
    onUpdatePosition: function (coordinate) {
      this.deviceCoordinate = coordinate
      this.center = [this.deviceCoordinate[0], this.deviceCoordinate[1]]
    },
    onUpdateAccuracy: function (accuracy) {
      this.coordinateAccuracy = accuracy
    },
    address2Geoloc () {
      // 1 East Edenton St, Raleigh, NC, USA
      geocoder.search({ q: this.address })
        .then((response) => {
          this.getlocation = 'False'
          this.currentlocation = 'False'
          this.addresslocation = 'True'
          this.center = [Number(response[0].lon), Number(response[0].lat)]
          this.addressloc = [Number(response[0].lon), Number(response[0].lat)]
        })
        .catch((error) => {
          console.log(error)
        })
    },
    resetAddress () {
      this.address = null
      this.acceptaddress = false
    },
    /* onRadarChartAction (params) {
      // console.log(params)
      const { origin, act, payload } = params
      let dothing
      if (this.dimensions[payload] === 'As') {
        dothing = 'Parts Per Million'
      } else if (this.dimensions[payload] === 'Cd') {
        dothing = 'Parts Per Million'
      } else if (this.dimensions[payload] === 'Pb') {
        dothing = 'Parts Per Million'
      } else if (this.dimensions[payload] === 'Mn') {
        dothing = 'Parts Per Thousand'
      }

      switch (act) {
        case origin.ACT_CLICK:
          alert(`Region ${payload} clicked`)
          break
        case origin.ACT_CLICK_DIMENSION_LABEL:
          alert(this.dimensions[payload] + ' ' + dothing)
          break
        default:
          break
      }
    }, */
    getColors: function (data, values, colors) {
      if (colors.length === 7) {
        if (data[this.currentvariable] === values[0]) {
          this.varcolor = colors[0]
        } else if (data[this.currentvariable] < values[1]) {
          this.varcolor = colors[1]
        } else if (data[this.currentvariable] >= values[1] && data[this.currentvariable] < values[2]) {
          this.varcolor = colors[2]
        } else if (data[this.currentvariable] >= values[2] && data[this.currentvariable] < values[3]) {
          this.varcolor = colors[3]
        } else if (data[this.currentvariable] >= values[3] && data[this.currentvariable] < values[4]) {
          this.varcolor = colors[4]
        } else if (data[this.currentvariable] >= values[4] && data[this.currentvariable] < values[5]) {
          this.varcolor = colors[5]
        } else if (data[this.currentvariable] >= values[5]) {
          this.varcolor = colors[6]
        }
      } else if (colors.length === 6) {
        if (data[this.currentvariable.substring(11)] === values[0]) {
          this.varcolor = colors[0]
        } else if (data[this.currentvariable.substring(11)] < values[1]) {
          this.varcolor = colors[1]
        } else if (data[this.currentvariable.substring(11)] >= values[1] && data[this.currentvariable.substring(11)] < values[2]) {
          this.varcolor = colors[2]
        } else if (data[this.currentvariable.substring(11)] >= values[2] && data[this.currentvariable.substring(11)] < values[3]) {
          this.varcolor = colors[3]
        } else if (data[this.currentvariable.substring(11)] >= values[3] && data[this.currentvariable.substring(11)] < values[4]) {
          this.varcolor = colors[4]
        } else if (data[this.currentvariable.substring(11)] >= values[4]) {
          this.varcolor = colors[5]
        }
      }
    },
    getncwellwiseStyle: function () {
      return feature => {
        let selected = !!this.vtSelection[feature.get(this.vtIdProp)]
        let data = feature.getProperties()
        let values
        if (this.currentvariable === 'ncwellwise_arsenic_med') {
          values = [-999.99, 6.83, 10.12, 13.42, 16.71]
          this.getColors(data, values, this.arsncolors)
        } else if (this.currentvariable === 'ncwellwise_arsenic_mean') {
          values = [-999.99, 8.95, 14.93, 20.93, 26.9]
          this.getColors(data, values, this.arsncolors)
        } else if (this.currentvariable === 'ncwellwise_arsenic_prcast') {
          values = [-999.99, 16.0, 32.0, 48.0, 64.0]
          this.getColors(data, values, this.arsncolors)
        } else if (this.currentvariable === 'ncwellwise_cadmium_med') {
          values = [-999.99, 0.74, 0.77, 0.79, 0.82]
          this.getColors(data, values, this.cadmcolors)
        } else if (this.currentvariable === 'ncwellwise_cadmium_mean') {
          values = [-999.99, 2.71, 4.72, 6.71, 8.73]
          this.getColors(data, values, this.cadmcolors)
        } else if (this.currentvariable === 'ncwellwise_cadmium_prcast') {
          values = [-999.99, 4.0, 8.0, 12.0, 16.0]
          this.getColors(data, values, this.cadmcolors)
        } else if (this.currentvariable === 'ncwellwise_lead_med') {
          values = [-999.99, 11.69, 19.83, 27.98, 36.12]
          this.getColors(data, values, this.leadcolors)
        } else if (this.currentvariable === 'ncwellwise_lead_mean') {
          values = [-999.99, 39.22, 75.53, 111.93, 148.14]
          this.getColors(data, values, this.leadcolors)
        } else if (this.currentvariable === 'ncwellwise_lead_prcast') {
          values = [-999.99, 20.0, 40.0, 60.0, 80.0]
          this.getColors(data, values, this.leadcolors)
        } else if (this.currentvariable === 'ncwellwise_manganese_med') {
          values = [-999.99, 184.4, 350.8, 517.2, 683.6]
          this.getColors(data, values, this.mngncolors)
        } else if (this.currentvariable === 'ncwellwise_manganese_mean') {
          values = [-999.99, 213.09, 404.97, 596.85, 788.73]
          this.getColors(data, values, this.mngncolors)
        } else if (this.currentvariable === 'ncwellwise_manganese_prcast') {
          values = [-999.99, 20.0, 40.0, 60.0, 80.0]
          this.getColors(data, values, this.mngncolors)
        }
        return [
          new Style({
            stroke: new Stroke({
              color: selected ? 'rgba(200,20,20,0.8)' : 'black',
              width: selected ? 2 : (this.zoom / 8.0)
            }),
            fill: new Fill({
              color: selected ? 'rgba(200,20,20,0.2)' : this.varcolor
            })
          })
        ]
      }
    },
    getacsStyle: function () {
      // console.log(this.currentvariable)
      return feature => {
        let selected = !!this.vtSelection[feature.get(this.vtIdProp)]
        let data = feature.getProperties()
        let values = [-999.99, 15, 30, 45, 60, 75]
        this.getColors(data, values, this.acscolors)
        return [
          new Style({
            stroke: new Stroke({
              color: selected ? 'rgba(200,20,20,0.8)' : 'black',
              width: selected ? 2 : (this.zoom / 8.0)
            }),
            fill: new Fill({
              color: selected ? 'rgba(200,20,20,0.2)' : this.varcolor
            })
          })
        ]
      }
    },
    getejscreenStyle: function () {
      // console.log(this.currentvariable)
      return feature => {
        let selected = !!this.vtSelection[feature.get(this.vtIdProp)]
        let data = feature.getProperties()
        let values
        if (this.currentvariable === 'd_ldpnt_2') {
          values = [-99999.9999, -200.0, 0.0, 200.0, 400.0, 600.0]
          this.getColors(data, values, this.ejscolors)
        } else if (this.currentvariable === 'd_dslpm_2') {
          values = [-99999.9999, -300.0, 0.0, 280.0, 580.0, 850.0]
          this.getColors(data, values, this.ejscolors)
        } else if (this.currentvariable === 'd_cancr_2') {
          values = [-99999.9999, -45000.0, -20000.0, 5000.0, 30000.0, 55000.0]
          this.getColors(data, values, this.ejscolors)
        } else if (this.currentvariable === 'd_resp_2') {
          values = [-99999.9999, -600.0, -250.0, 100.0, 450.0, 800.0]
          this.getColors(data, values, this.ejscolors)
        } else if (this.currentvariable === 'd_ptraf_2') {
          values = [-99999.9999, 800000.0, 1700000.0, 2600000.0, 3500000.0, 4400000.0]
          this.getColors(data, values, this.ejscolors)
        } else if (this.currentvariable === 'd_pwdis_2') {
          values = [-99999.9999, -47000.0, -35000.0, -22000.0, -10000.0, 200.0]
          this.getColors(data, values, this.ejscolors)
        } else if (this.currentvariable === 'd_pnpl_2') {
          values = [-99999.9999, -400.0, -120.0, 150.0, 420.0, 690.0]
          this.getColors(data, values, this.ejscolors)
        } else if (this.currentvariable === 'd_prmp_2') {
          values = [-99999.9999, -450.0, 1000.0, 2450.0, 3900.0, 5350.0]
          this.getColors(data, values, this.ejscolors)
        } else if (this.currentvariable === 'd_ptsdf_2') {
          values = [-99999.9999, -3200.0, -1000.0, 1800.0, 4600.0, 7300.0]
          this.getColors(data, values, this.ejscolors)
        } else if (this.currentvariable === 'd_ozone_2') {
          values = [-99999.9999, -58000.0, -28000.0, 600.0, 38000.0, 70000.0]
          this.getColors(data, values, this.ejscolors)
        } else if (this.currentvariable === 'd_pm25_2') {
          values = [-99999.9999, -11000.0, -5500.0, 1000.0, 7500.0, 15000.0]
          this.getColors(data, values, this.ejscolors)
        }
        return [
          new Style({
            stroke: new Stroke({
              color: selected ? 'rgba(200,20,20,0.8)' : 'black',
              width: selected ? 2 : (this.zoom / 8.0)
            }),
            fill: new Fill({
              color: selected ? 'rgba(200,20,20,0.2)' : this.varcolor
            })
          })
        ]
      }
    },
    getcovid19Style: function () {
      // console.log(this.currentvariable)
      return feature => {
        let selected = !!this.vtSelection[feature.get(this.vtIdProp)]
        let data = feature.getProperties()
        let values
        if (this.currentvariable === 'cases') {
          values = [-999.99, 1328, 2656, 3984, 5416, 6644]
          this.getColors(data, values, this.covidcolors)
        } else if (this.currentvariable === 'cases_per_10000_res') {
          values = [-999.99, 586.0, 1172.0, 1758.0, 2344.0, 2930.0]
          this.getColors(data, values, this.covidcolors)
        } else if (this.currentvariable === 'cases_per_100000_res') {
          values = [-999.99, 5859.0, 11718.0, 17577.0, 23436.0, 29295.0]
          this.getColors(data, values, this.covidcolors)
        } else if (this.currentvariable === 'deaths') {
          values = [-999.99, 17, 34, 51, 65, 85]
          this.getColors(data, values, this.covidcolors)
        }
        return [
          new Style({
            stroke: new Stroke({
              color: selected ? 'rgba(200,20,20,0.8)' : 'black',
              width: selected ? 2 : (this.zoom / 8.0)
            }),
            fill: new Fill({
              color: selected ? 'rgba(200,20,20,0.2)' : this.varcolor
            })
          })
        ]
      }
    },
    getNCCountiesStyle: function () {
      return feature => {
        return [
          createStyle({
            strokeColor: '#000',
            strokeWidth: (this.zoom / 4.0),
            strokeLineCap: 'round',
            strokeLineJoin: 'bevel'
          })
        ]
      }
    },
    getNoLayerStyle: function () {
      return feature => {
        return [
          createStyle({
            strokeColor: 'rgba(200,20,20,0.0)',
            strokeWidth: (this.zoom / 10.0),
            strokeLineCap: 'round',
            strokeLineJoin: 'bevel'
          })
        ]
      }
    },
    getNCWellwiseLayerID: function () {
      return 'ncwellwise'
    },
    getACSCensusLayerID: function () {
      return 'acs_census'
    },
    getEJScreenLayerID: function () {
      return 'ejscreen'
    },
    getCovid19LayerID: function () {
      return 'covid19'
    },
    onMapMounted: function (map) {
      // now ol.Map instance is ready and we can work with it directly
      this.$refs.map.$map.getControls().extend([
        new ScaleLine({
          target: 'ScaleTarget'
        }),
        new OverviewMap({
          collapsed: false,
          collapsible: true,
          target: 'OverviewMapTarget'
        }),
        new Zoom({
          target: 'ZoomTarget'
        }),
        new Attribution({
          collapsed: false,
          collapsible: false,
          target: 'AttributionTarget'
        })
      ])
    },
    closeBarChart: function () {
      this.selectedFeature = this.selectedFeature.filter(f => f.id === 0)
      let drawFeatures = this.$refs.drawSource.getFeatures()
      // console.log(drawFeatures)
      this.$refs.drawSource.removeFeatures(drawFeatures)
    },
    // base layers
    showBaseLayer: function () {
      let layer = this.baseLayers.find(layer => layer.visible)
      if (layer != null) {
        layer.visible = false
      }

      layer = this.baseLayers.find(layer => layer.name === this.baselayer)
      if (layer != null) {
        layer.visible = true
      }
    },
    showMapPanelToggleLayer: function () {
      let cntlayer = this.layers[4]
      if (this.ncCountiesModel === 'Selected') {
        cntlayer.visible = true
      } else if (this.ncCountiesModel === 'Not Selected') {
        cntlayer.visible = false
      }
    },
    showMapPanelRadioLayer: function () {
      let layer = this.layers.find(layer => layer.visible)

      if (layer != null) {
        layer.visible = false
      }

      var i
      if (this.currentvariable === 'ncwellwise_arsenic_med') {
        layer = this.layers.find(layer => layer.id === 'ncwellwise')
        for (i = 0; i < this.$refs.layerStyle.length; i++) { this.$refs.layerStyle[i].refresh() }
        // this.$refs.layerStyle.refresh()
      } else if (this.currentvariable === 'ncwellwise_arsenic_mean') {
        layer = this.layers.find(layer => layer.id === 'ncwellwise')
        for (i = 0; i < this.$refs.layerStyle.length; i++) { this.$refs.layerStyle[i].refresh() }
        // this.$refs.layerStyle.refresh()
      } else if (this.currentvariable === 'ncwellwise_arsenic_prcast') {
        layer = this.layers.find(layer => layer.id === 'ncwellwise')
        for (i = 0; i < this.$refs.layerStyle.length; i++) { this.$refs.layerStyle[i].refresh() }
        // this.$refs.layerStyle.refresh()
      } else if (this.currentvariable === 'ncwellwise_cadmium_med') {
        layer = this.layers.find(layer => layer.id === 'ncwellwise')
        for (i = 0; i < this.$refs.layerStyle.length; i++) { this.$refs.layerStyle[i].refresh() }
        // this.$refs.layerStyle.refresh()
      } else if (this.currentvariable === 'ncwellwise_cadmium_mean') {
        layer = this.layers.find(layer => layer.id === 'ncwellwise')
        for (i = 0; i < this.$refs.layerStyle.length; i++) { this.$refs.layerStyle[i].refresh() }
        // this.$refs.layerStyle.refresh()
      } else if (this.currentvariable === 'ncwellwise_cadmium_prcast') {
        layer = this.layers.find(layer => layer.id === 'ncwellwise')
        for (i = 0; i < this.$refs.layerStyle.length; i++) { this.$refs.layerStyle[i].refresh() }
        // this.$refs.layerStyle.refresh()
      } else if (this.currentvariable === 'ncwellwise_lead_med') {
        layer = this.layers.find(layer => layer.id === 'ncwellwise')
        for (i = 0; i < this.$refs.layerStyle.length; i++) { this.$refs.layerStyle[i].refresh() }
        // this.$refs.layerStyle.refresh()
      } else if (this.currentvariable === 'ncwellwise_lead_mean') {
        layer = this.layers.find(layer => layer.id === 'ncwellwise')
        for (i = 0; i < this.$refs.layerStyle.length; i++) { this.$refs.layerStyle[i].refresh() }
        // this.$refs.layerStyle.refresh()
      } else if (this.currentvariable === 'ncwellwise_lead_prcast') {
        layer = this.layers.find(layer => layer.id === 'ncwellwise')
        for (i = 0; i < this.$refs.layerStyle.length; i++) { this.$refs.layerStyle[i].refresh() }
        // this.$refs.layerStyle.refresh()
      } else if (this.currentvariable === 'ncwellwise_manganese_med') {
        layer = this.layers.find(layer => layer.id === 'ncwellwise')
        for (i = 0; i < this.$refs.layerStyle.length; i++) { this.$refs.layerStyle[i].refresh() }
        // this.$refs.layerStyle.refresh()
      } else if (this.currentvariable === 'ncwellwise_manganese_mean') {
        layer = this.layers.find(layer => layer.id === 'ncwellwise')
        for (i = 0; i < this.$refs.layerStyle.length; i++) { this.$refs.layerStyle[i].refresh() }
        // this.$refs.layerStyle.refresh()
      } else if (this.currentvariable === 'ncwellwise_manganese_prcast') {
        layer = this.layers.find(layer => layer.id === 'ncwellwise')
        for (i = 0; i < this.$refs.layerStyle.length; i++) { this.$refs.layerStyle[i].refresh() }
        // this.$refs.layerStyle.refresh()
      } else if (this.currentvariable === 'percent_below_poverty_level') {
        layer = this.layers.find(layer => layer.id === 'acs_census')
        for (i = 0; i < this.$refs.layerStyle.length; i++) { this.$refs.layerStyle[i].refresh() }
        // this.$refs.layerStyle.refresh()
      } else if (this.currentvariable === 'percent_below_poverty_level') {
        layer = this.layers.find(layer => layer.id === 'acs_census')
        for (i = 0; i < this.$refs.layerStyle.length; i++) { this.$refs.layerStyle[i].refresh() }
        // this.$refs.layerStyle.refresh()
      } else if (this.currentvariable === 'speak_a_language_other_than_english') {
        layer = this.layers.find(layer => layer.id === 'acs_census')
        for (i = 0; i < this.$refs.layerStyle.length; i++) { this.$refs.layerStyle[i].refresh() }
        // this.$refs.layerStyle.refresh()
      } else if (this.currentvariable === 'two_or_more_races') {
        layer = this.layers.find(layer => layer.id === 'acs_census')
        for (i = 0; i < this.$refs.layerStyle.length; i++) { this.$refs.layerStyle[i].refresh() }
        // this.$refs.layerStyle.refresh()
      } else if (this.currentvariable === 'asian_alone') {
        layer = this.layers.find(layer => layer.id === 'acs_census')
        for (i = 0; i < this.$refs.layerStyle.length; i++) { this.$refs.layerStyle[i].refresh() }
        // this.$refs.layerStyle.refresh()
      } else if (this.currentvariable === 'american_indian_and_alaska_native_alone') {
        layer = this.layers.find(layer => layer.id === 'acs_census')
        for (i = 0; i < this.$refs.layerStyle.length; i++) { this.$refs.layerStyle[i].refresh() }
        // this.$refs.layerStyle.refresh()
      } else if (this.currentvariable === 'native_hawaiian_and_other_pacific_islander_alone') {
        layer = this.layers.find(layer => layer.id === 'acs_census')
        for (i = 0; i < this.$refs.layerStyle.length; i++) { this.$refs.layerStyle[i].refresh() }
        // this.$refs.layerStyle.refresh()
      } else if (this.currentvariable === 'white_alone') {
        layer = this.layers.find(layer => layer.id === 'acs_census')
        for (i = 0; i < this.$refs.layerStyle.length; i++) { this.$refs.layerStyle[i].refresh() }
        // this.$refs.layerStyle.refresh()
      } else if (this.currentvariable === 'black_or_african_american_alone') {
        layer = this.layers.find(layer => layer.id === 'acs_census')
        for (i = 0; i < this.$refs.layerStyle.length; i++) { this.$refs.layerStyle[i].refresh() }
        // this.$refs.layerStyle.refresh()
      } else if (this.currentvariable === 'not_hispanic_or_latino') {
        layer = this.layers.find(layer => layer.id === 'acs_census')
        for (i = 0; i < this.$refs.layerStyle.length; i++) { this.$refs.layerStyle[i].refresh() }
        // this.$refs.layerStyle.refresh()
      } else if (this.currentvariable === 'hispanic_or_latino_of_any_race') {
        layer = this.layers.find(layer => layer.id === 'acs_census')
        for (i = 0; i < this.$refs.layerStyle.length; i++) { this.$refs.layerStyle[i].refresh() }
        // this.$refs.layerStyle.refresh()
      } else if (this.currentvariable === 'd_ldpnt_2') {
        layer = this.layers.find(layer => layer.id === 'ejscreen')
        for (i = 0; i < this.$refs.layerStyle.length; i++) { this.$refs.layerStyle[i].refresh() }
        // this.$refs.layerStyle.refresh()
      } else if (this.currentvariable === 'd_dslpm_2') {
        layer = this.layers.find(layer => layer.id === 'ejscreen')
        for (i = 0; i < this.$refs.layerStyle.length; i++) { this.$refs.layerStyle[i].refresh() }
        // this.$refs.layerStyle.refresh()
      } else if (this.currentvariable === 'd_cancr_2') {
        layer = this.layers.find(layer => layer.id === 'ejscreen')
        for (i = 0; i < this.$refs.layerStyle.length; i++) { this.$refs.layerStyle[i].refresh() }
        // this.$refs.layerStyle.refresh()
      } else if (this.currentvariable === 'd_resp_2') {
        layer = this.layers.find(layer => layer.id === 'ejscreen')
        for (i = 0; i < this.$refs.layerStyle.length; i++) { this.$refs.layerStyle[i].refresh() }
        // this.$refs.layerStyle.refresh()
      } else if (this.currentvariable === 'd_ptraf_2') {
        layer = this.layers.find(layer => layer.id === 'ejscreen')
        for (i = 0; i < this.$refs.layerStyle.length; i++) { this.$refs.layerStyle[i].refresh() }
        // this.$refs.layerStyle.refresh()
      } else if (this.currentvariable === 'd_pwdis_2') {
        layer = this.layers.find(layer => layer.id === 'ejscreen')
        for (i = 0; i < this.$refs.layerStyle.length; i++) { this.$refs.layerStyle[i].refresh() }
        // this.$refs.layerStyle.refresh()
      } else if (this.currentvariable === 'd_pnpl_2') {
        layer = this.layers.find(layer => layer.id === 'ejscreen')
        for (i = 0; i < this.$refs.layerStyle.length; i++) { this.$refs.layerStyle[i].refresh() }
        // this.$refs.layerStyle.refresh()
      } else if (this.currentvariable === 'd_prmp_2') {
        layer = this.layers.find(layer => layer.id === 'ejscreen')
        for (i = 0; i < this.$refs.layerStyle.length; i++) { this.$refs.layerStyle[i].refresh() }
        // this.$refs.layerStyle.refresh()
      } else if (this.currentvariable === 'd_ptsdf_2') {
        layer = this.layers.find(layer => layer.id === 'ejscreen')
        for (i = 0; i < this.$refs.layerStyle.length; i++) { this.$refs.layerStyle[i].refresh() }
        // this.$refs.layerStyle.refresh()
      } else if (this.currentvariable === 'd_ozone_2') {
        layer = this.layers.find(layer => layer.id === 'ejscreen')
        for (i = 0; i < this.$refs.layerStyle.length; i++) { this.$refs.layerStyle[i].refresh() }
        // this.$refs.layerStyle.refresh()
      } else if (this.currentvariable === 'd_pm25_2') {
        layer = this.layers.find(layer => layer.id === 'ejscreen')
        for (i = 0; i < this.$refs.layerStyle.length; i++) { this.$refs.layerStyle[i].refresh() }
        // this.$refs.layerStyle.refresh()
      } else if (this.currentvariable === 'cases') {
        layer = this.layers.find(layer => layer.id === 'covid19')
        for (i = 0; i < this.$refs.layerStyle.length; i++) { this.$refs.layerStyle[i].refresh() }
        // this.$refs.layerStyle.refresh()
      } else if (this.currentvariable === 'cases_per_10000_res') {
        layer = this.layers.find(layer => layer.id === 'covid19')
        for (i = 0; i < this.$refs.layerStyle.length; i++) { this.$refs.layerStyle[i].refresh() }
        // this.$refs.layerStyle.refresh()
      } else if (this.currentvariable === 'cases_per_100000_res') {
        layer = this.layers.find(layer => layer.id === 'covid19')
        for (i = 0; i < this.$refs.layerStyle.length; i++) { this.$refs.layerStyle[i].refresh() }
        // this.$refs.layerStyle.refresh()
      } else if (this.currentvariable === 'deaths') {
        layer = this.layers.find(layer => layer.id === 'covid19')
        for (i = 0; i < this.$refs.layerStyle.length; i++) { this.$refs.layerStyle[i].refresh() }
        // this.$refs.layerStyle.refresh()
      } else if (this.currentvariable === 'nolayer') {
        layer = this.layers.find(layer => layer.id === 'noLayer')
        for (i = 0; i < this.$refs.layerStyle.length; i++) { this.$refs.layerStyle[i].refresh() }
        // this.$refs.layerStyle.refresh()
      }
      // console.log(this.$refs.layerStyle)
      if (layer != null) {
        layer.visible = true
      }
    },
    onMapClick: function (event) {
      let pixel = event.pixel
      let features = this.$refs.map.$map.getFeaturesAtPixel(pixel)
      let layer = this.layers.find(layer => layer.visible)
      if (!features) {
        this.vtSelection = {}
        this.selectedFeatureMeanBarBox = []
        this.selectedFeatureMedBarBox = []
        this.selectedFeaturePrcastBarBox = []
        this.selectedFeatureMinBarBox = []
        this.selectedFeatureMaxBarBox = []
        this.selectedFeatureStdBarBox = []
        this.selectedFeature = []
        this.$refs.layerStyle[0].refresh()
        // this.$refs.layerStyle.refresh()
      } else if (features) {
        if (layer.id === 'ncwellwise') {
          this.vtSelection = {}
          this.selectedFeatureMeanBarBox = []
          this.selectedFeatureMedBarBox = []
          this.selectedFeaturePrcastBarBox = []
          this.selectedFeatureMinBarBox = []
          this.selectedFeatureMaxBarBox = []
          this.selectedFeatureStdBarBox = []
          this.eventCoordinate = event.coordinate
          let feature = features[0]
          let fid = feature.get(this.vtIdProp)
          this.vtSelection[fid] = feature
          let properties = feature.getProperties()
          if (properties['geoid10']) {
            this.pid = properties['geoid10']
            this.selectedFeatureMedBarBox.push(properties['arsenic_med'])
            this.selectedFeatureMedBarBox.push(properties['cadmium_med'])
            this.selectedFeatureMedBarBox.push(properties['lead_med'])
            this.selectedFeatureMedBarBox.push(properties['manganese_med'])
            this.selectedFeatureMeanBarBox.push(properties['arsenic_mean'])
            this.selectedFeatureMeanBarBox.push(properties['cadmium_mean'])
            this.selectedFeatureMeanBarBox.push(properties['lead_mean'])
            this.selectedFeatureMeanBarBox.push(properties['manganese_mean'])
            this.selectedFeaturePrcastBarBox.push(properties['arsenic_prcast'])
            this.selectedFeaturePrcastBarBox.push(properties['cadmium_prcast'])
            this.selectedFeaturePrcastBarBox.push(properties['lead_prcast'])
            this.selectedFeaturePrcastBarBox.push(properties['manganese_prcast'])
            this.selectedFeatureMinBarBox.push(properties['arsenic_minimum'])
            this.selectedFeatureMinBarBox.push(properties['cadmium_minimum'])
            this.selectedFeatureMinBarBox.push(properties['lead_minimum'])
            this.selectedFeatureMinBarBox.push(properties['manganese_minimum'])
            this.selectedFeatureMaxBarBox.push(properties['arsenic_maximum'])
            this.selectedFeatureMaxBarBox.push(properties['cadmium_med'])
            this.selectedFeatureMaxBarBox.push(properties['lead_maximum'])
            this.selectedFeatureMaxBarBox.push(properties['manganese_maximum'])
            this.selectedFeatureStdBarBox.push(properties['arsenic_std'])
            this.selectedFeatureStdBarBox.push(properties['cadmium_std'])
            this.selectedFeatureStdBarBox.push(properties['lead_std'])
            this.selectedFeatureStdBarBox.push(properties['manganese_std'])
          }
          this.$refs.layerStyle[0].refresh()
          // this.$refs.layerStyle.refresh()
        }
      }
    }
  }
}
</script>

<style lang="scss">
  .ol-control button {
    color: black;
    background-color: rgb(0,128,128);
  }
  .ol-control button:hover {
    text-decoration: none;
    background-color: rgb(0,128,128);
  }
  .ol-control button:focus {
    text-decoration: none;
    background-color: rgb(0,128,128);
  }
  .ol-control button:hover, {
    text-decoration: none;
    background-color: rgba(0,128,128,0.8);
  }
  .ol-control button:focus {
    text-decoration: none;
    background-color: rgba(0,128,128,0.8);
  }
  .ol-scale-line {
    background: rgba(0,128,128,0.8);
  }
  a:hover {
    font-weight:bold;
  }
  .wrapper {
    display: flex;
  }
  .map {
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
  }
  .view {
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
  }
  .feature-popup {
    position: absolute;
    left: -20px;
    bottom: 12px;
    width: 32em;
    max-width: none;
  }
  .feature-popup:after, .feature-popup:before {
    top: 100%;
    border: solid transparent;
    content: ' ';
    height: 0;
    width: 0;
    position: absolute;
    pointer-events: none;
  }
  .feature-popup:after {
    border-top-color: white;
    border-width: 10px;
    left: 48px;
    margin-left: -10px;
  }
  .feature-popup:before {
    border-top-color: #cccccc;
    border-width: 11px;
    left: 48px;
    margin-left: -11px;
  }
  .feature-popup .card-content {
    max-height: 20em;
    overflow: auto;
  }
  .feature-popup .content {
    word-break: break-all;
  }
  .squfill {
    height: 15px;
    width: 15px;
    background-color: rgba(91, 95, 99, 0.65);
    display: inline-block;
  }
  .pbsqufill {
    height: 15px;
    width: 15px;
    background-color: rgba(50, 110, 219, 0.65);
    display: inline-block;
  }
  .assqu1 {
    height: 15px;
    width: 15px;
    background-color: rgba(235, 52, 220, 0.65);
    display: inline-block;
  }
  .assqu2 {
    height: 15px;
    width: 15px;
    background-color: rgba(186, 52, 235, 0.65);
    display: inline-block;
  }
  .assqu3 {
    height: 15px;
    width: 15px;
    background-color: rgba(165, 52, 235, 0.65);
    display: inline-block;
  }
  .assqu4 {
    height: 15px;
    width: 15px;
    background-color: rgba(143, 52, 235, 0.65);
    display: inline-block;
  }
  .assqu5 {
    height: 15px;
    width: 15px;
    background-color: rgba(119, 52, 235, 0.65);
    display: inline-block;
  }
  .cdsqu5 {
    height: 15px;
    width: 15px;
    background-color: rgba(235, 89, 52, 0.65);
    display: inline-block;
  }
  .cdsqu4 {
    height: 15px;
    width: 15px;
    background-color: rgba(235, 131, 52, 0.65);
    display: inline-block;
  }
  .cdsqu3 {
    height: 15px;
    width: 15px;
    background-color: rgba(235, 162, 52, 0.65);
    display: inline-block;
  }
  .cdsqu2 {
    height: 15px;
    width: 15px;
    background-color: rgba(235, 192, 52, 0.65);
    display: inline-block;
  }
  .cdsqu1 {
    height: 15px;
    width: 15px;
    background-color: rgba(223, 235, 52, 0.65);
    display: inline-block;
  }
  .pbsqu1 {
    height: 15px;
    width: 15px;
    background-color: rgba(196, 200, 207, 0.65);
    display: inline-block;
  }
  .pbsqu2 {
    height: 15px;
    width: 15px;
    background-color: rgba(156, 162, 173, 0.65);
    display: inline-block;
  }
  .pbsqu3 {
    height: 15px;
    width: 15px;
    background-color: rgba(116, 121, 130, 0.65);
    display: inline-block;
  }
  .pbsqu4 {
    height: 15px;
    width: 15px;
    background-color: rgba(79, 82, 89, 0.65);
    display: inline-block;
  }
  .pbsqu5 {
    height: 15px;
    width: 15px;
    background-color: rgba(39, 40, 43, 0.65);
    display: inline-block;
  }
  .mnsqu1 {
    height: 15px;
    width: 15px;
    background-color: rgba(194, 232, 190, 0.65);
    display: inline-block;
  }
  .mnsqu2 {
    height: 15px;
    width: 15px;
    background-color: rgba(81, 222, 67, 0.65);
    display: inline-block;
  }
  .mnsqu3 {
    height: 15px;
    width: 15px;
    background-color: rgba(25, 128, 11, 0.65);
    display: inline-block;
  }
  .mnsqu4 {
    height: 15px;
    width: 15px;
    background-color: rgba(14, 82, 5, 0.65);
    display: inline-block;
  }
  .mnsqu5 {
    height: 15px;
    width: 15px;
    background-color: rgba(5, 97, 76, 0.65);
    display: inline-block;
  }
  .acssqu1 {
    height: 15px;
    width: 15px;
    background-color: rgba(252, 210, 211, 0.65);
    display: inline-block;
  }
  .acssqu2 {
    height: 15px;
    width: 15px;
    background-color: rgba(252, 109, 114, 0.65);
    display: inline-block;
  }
  .acssqu3 {
    height: 15px;
    width: 15px;
    background-color: rgba(247, 59, 66, 0.65);
    display: inline-block;
  }
  .acssqu4 {
    height: 15px;
    width: 15px;
    background-color: rgba(250, 2, 11, 0.65);
    display: inline-block;
  }
  .acssqu5 {
    height: 15px;
    width: 15px;
    background-color: rgba(181, 2, 6, 0.65);
    display: inline-block;
  }
  .acssqu6 {
    height: 15px;
    width: 15px;
    background-color: rgba(140, 1, 5, 0.65);
    display: inline-block;
  }
  .heasqu1 {
    height: 15px;
    width: 15px;
    background-color: rgba(34, 240, 219, 0.65);
    display: inline-block;
  }
  .heasqu2 {
    height: 15px;
    width: 15px;
    background-color: rgba(34, 223, 240, 0.65);
    display: inline-block;
  }
  .heasqu3 {
    height: 15px;
    width: 15px;
    background-color: rgba(34, 185, 240, 0.65);
    display: inline-block;
  }
  .heasqu4 {
    height: 15px;
    width: 15px;
    background-color: rgba(22, 141, 245, 0.65);
    display: inline-block;
  }
  .heasqu5 {
    height: 15px;
    width: 15px;
    background-color: rgba(22, 74, 245, 0.65);
    display: inline-block;
  }
  .heasqu6 {
    height: 15px;
    width: 15px;
    background-color: rgba(23, 2, 247, 0.65);
    display: inline-block;
  }
  .ejssqu1 {
    height: 15px;
    width: 15px;
    background-color: rgba(235, 252, 3, 0.65);
    display: inline-block;
  }
  .ejssqu2 {
    height: 15px;
    width: 15px;
    background-color: rgba(252, 227, 3, 0.65);
    display: inline-block;
  }
  .ejssqu3 {
    height: 15px;
    width: 15px;
    background-color: rgba(252, 186, 3, 0.65);
    display: inline-block;
  }
  .ejssqu4 {
    height: 15px;
    width: 15px;
    background-color: rgba(252, 128, 3, 0.65);
    display: inline-block;
  }
  .ejssqu5 {
    height: 15px;
    width: 15px;
    background-color: rgba(252, 82, 3, 0.65);
    display: inline-block;
  }
  .ejssqu6 {
    height: 15px;
    width: 15px;
    background-color: rgba(140, 1, 5, 0.65);
    display: inline-block;
  }
  .q-input {
    height: 4.0em;
  }
  .q-select {
    height: 4.0em;
  }
</style>
