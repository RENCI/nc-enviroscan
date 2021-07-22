<template>
  <q-layout view="lhr lpr lfr">
    <!--// Left Drawer Starts-->
    <q-drawer v-model="leftDrawerOpen" :width="320" show-if-above bordered :content-style="{ backgroundColor: 'rgba(199, 235, 235, 0.5)' }">
      <font size="4" face="Arial" >
        <div style="text-align:center">Census Tract Details</div>
      </font>
      <q-space />
      <q-separator />
      <q-space />
      <center>
        <q-card class="q-pa-md bg-teal-1" style="max-width: 300px">
          <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">Click Census tract feature in map to display graph</q-tooltip>
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
      </center>
      <q-space />
      <q-separator />
      <q-space />
      <center>
        <q-card class="q-pa-md bg-teal-1" style="max-width: 300px">
          <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">Click Census tract feature in map to display graph</q-tooltip>
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
      </center>
      <q-space />
      <q-separator />
      <q-space />
      <center>
        <q-card class="q-pa-md bg-teal-1" style="max-width: 300px">
          <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">Click Census tract feature in map to display graph</q-tooltip>
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
      </center>
      <q-space />
      <q-separator />
      <q-space />
      <center>
        <q-card class="q-pa-md bg-teal-1" style="max-width: 300px">
          <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">Click Census tract feature in map to display graph</q-tooltip>
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
      </center>
      <q-space />
      <q-separator />
      <q-space />
      <center>
        <q-card class="q-pa-md bg-teal-1" style="max-width: 300px">
          <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">Click Census tract feature in map to display graph</q-tooltip>
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
      </center>
      <q-space />
      <q-separator />
      <q-space />
      <center>
        <q-card class="q-pa-md bg-teal-1" style="max-width: 300px">
          <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">Click Census tract feature in map to display graph</q-tooltip>
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
      </center>
    </q-drawer>
    <!--// Left Drawer Ends -->

    <!--// right side drawer Starts -->
    <q-drawer side="right" v-model="rightDrawerOpen" :width="400" show-if-above bordered content-class="teal bg-teal-1">
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
        <q-expansion-item expand-separator icon="list" label="Clear Data">
          <div class="q-pa-md" style="min-width: 200px">
            <q-list link>
              <q-item tag="label" v-ripple>
                <q-item-section avatar>
                  <q-radio v-on:input="showMapPanelRadioLayer" val="nolayer" v-model="currentvariable" color="teal" />
                </q-item-section>
                <q-item-section>
                  <q-item-label>Clear Data</q-item-label>
                </q-item-section>
              </q-item>
            </q-list>
          </div>
        </q-expansion-item>
        <!-- // nolayer -->

        <!-- // NC wellwise layers -->
        <q-expansion-item default-opened dense dense-toggle expand-separator icon="list" label="Environmental Indicators, by Census Tracts">
          <div class="q-pa-md q-gutter-y-sm column">
            <table cellspacing="0" cellpadding="0" style="width:100%">
              <tr>
                <td></td>
                <td>Median</td>
                <td>Mean</td>
                <td>% Above Standard</td>
                <td>Legend</td>
              </tr>
              <tr>
                <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">Arsenic (ppb and %)</q-tooltip>
                <td>Arsenic</td>
                <td><q-radio v-on:input="showMapPanelRadioLayer" val="ncwellwise_arsenic_med" v-model="currentvariable" color="teal" /></td>
                <td><q-radio v-on:input="showMapPanelRadioLayer" val="ncwellwise_arsenic_mean" v-model="currentvariable" color="teal" /></td>
                <td><q-radio v-on:input="showMapPanelRadioLayer" val="ncwellwise_arsenic_prcast" v-model="currentvariable" color="teal" /></td>
                <td>
                  <q-btn flat dense round icon="fas fa-list" class="teal text-black" aria-label="Map Legend">
                    <q-tooltip>Click to View Map Legend</q-tooltip>
                    <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
                      <font size="2" face="Arial" >
                        <q-markup-table dense class="bg-teal-1">
                          <tr>
                            <td style="text-align:center;" colspan="2">Median (ppb)</td>
                            <td style="text-align:center;" >Mean (ppb)</td>
                            <td style="text-align:center;" >% Above Standard</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="assqu1"></span></td>
                            <td>&gt; {{ arsenic_med_values[1] }}</td>
                            <td>&gt; {{ arsenic_mean_values[1] }}</td>
                            <td>&gt; {{ arsenic_prcast_values[1] }}</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="assqu2"></span></td>
                            <td>&ge; {{ arsenic_med_values[1] }} &amp; &lt; {{ arsenic_med_values[2] }}</td>
                            <td>&ge; {{ arsenic_mean_values[1] }} &amp; &lt; {{ arsenic_mean_values[2] }}</td>
                            <td>&ge; {{ arsenic_prcast_values[1] }} &amp; &lt; {{ arsenic_prcast_values[2] }}</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="assqu3"></span></td>
                            <td>&ge; {{ arsenic_med_values[2] }} &amp; &lt; {{ arsenic_med_values[3] }}</td>
                            <td>&ge; {{ arsenic_mean_values[2] }} &amp; &lt; {{ arsenic_mean_values[3] }}</td>
                            <td>&ge; {{ arsenic_prcast_values[2] }} &amp; &lt; {{ arsenic_prcast_values[3] }}</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="assqu4"></span></td>
                            <td>&ge; {{ arsenic_med_values[3] }}</td>
                            <td>&ge; {{ arsenic_mean_values[3] }}</td>
                            <td>&ge; {{ arsenic_prcast_values[3] }}</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="squfill"></span></td>
                            <td>No Data {{ arsenic_med_values[0] }}</td>
                          </tr>
                        </q-markup-table>
                      </font>
                    </q-popup-proxy>
                  </q-btn>
                </td>
              </tr>
              <tr>
                <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">Cadmium (ppb and %)</q-tooltip>
                <td>Cadmium</td>
                <td><q-radio v-on:input="showMapPanelRadioLayer" val="ncwellwise_cadmium_med" v-model="currentvariable" color="teal" /></td>
                <td><q-radio v-on:input="showMapPanelRadioLayer" val="ncwellwise_cadmium_mean" v-model="currentvariable" color="teal" /></td>
                <td><q-radio v-on:input="showMapPanelRadioLayer" val="ncwellwise_cadmium_prcast" v-model="currentvariable" color="teal" /></td>
                <td>
                  <q-btn flat dense round icon="fas fa-list" class="teal text-black" aria-label="Map Legend">
                    <q-tooltip>Click to View Map Legend</q-tooltip>
                    <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
                      <font size="2" face="Arial" >
                        <q-markup-table dense class="bg-teal-1">
                          <tr>
                            <td style="text-align:center;" colspan="2">Median (ppb)</td>
                            <td style="text-align:center;" >Mean (ppb)</td>
                            <td style="text-align:center;" >% Above Standard</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="cdsqu1"></span></td>
                            <td>&gt; {{ cadmium_med_values[1] }}</td>
                            <td>&gt; {{ cadmium_mean_values[1] }}</td>
                            <td>&gt; {{ cadmium_prcast_values[1] }}</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="cdsqu2"></span></td>
                            <td>&ge; {{ cadmium_med_values[1] }} &amp; &lt; {{ cadmium_med_values[2] }}</td>
                            <td>&ge; {{ cadmium_mean_values[1] }} &amp; &lt; {{ cadmium_mean_values[2] }}</td>
                            <td>&ge; {{ cadmium_mean_values[1] }} &amp; &lt; {{ cadmium_mean_values[2] }}</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="cdsqu3"></span></td>
                            <td>&ge; {{ cadmium_med_values[2] }} &amp; &lt; {{ cadmium_med_values[3] }}</td>
                            <td>&ge; {{ cadmium_mean_values[2] }} &amp; &lt; {{ cadmium_mean_values[3] }}</td>
                            <td>&ge; {{ cadmium_mean_values[2] }} &amp; &lt; {{ cadmium_mean_values[3] }}</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="cdsqu4"></span></td>
                            <td>&ge; {{ cadmium_med_values[3] }}</td>
                            <td>&ge; {{ cadmium_mean_values[3] }}</td>
                            <td>&ge; {{ cadmium_mean_values[3] }}</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="squfill"></span></td>
                            <td>No Data {{ cadmium_med_values[0] }}</td>
                          </tr>
                        </q-markup-table>
                      </font>
                    </q-popup-proxy>
                  </q-btn>
                </td>
              </tr>
              <tr>
                <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">Lead (ppb and %)</q-tooltip>
                <td>Lead</td>
                <td><q-radio v-on:input="showMapPanelRadioLayer" val="ncwellwise_lead_med" v-model="currentvariable" color="teal" /></td>
                <td><q-radio v-on:input="showMapPanelRadioLayer" val="ncwellwise_lead_mean" v-model="currentvariable" color="teal" /></td>
                <td><q-radio v-on:input="showMapPanelRadioLayer" val="ncwellwise_lead_prcast" v-model="currentvariable" color="teal" /></td>
                <td>
                  <q-btn flat dense round icon="fas fa-list" class="teal text-black" aria-label="Map Legend">
                    <q-tooltip>Click to View Map Legend</q-tooltip>
                    <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
                      <font size="2" face="Arial" >
                        <q-markup-table dense class="bg-teal-1">
                          <tr>
                             <td style="text-align:center;" colspan="2">Median (ppb)</td>
                             <td style="text-align:center;" >Mean (ppb)</td>
                             <td style="text-align:center;" >% Above Standard</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="pbsqu1"></span></td>
                            <td>&gt; {{ lead_med_values[1] }}</td>
                            <td>&gt; {{ lead_mean_values[1] }}</td>
                            <td>&gt; {{ lead_prcast_values[1] }}</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="pbsqu2"></span></td>
                            <td>&ge; {{ lead_med_values[1] }} &amp; &lt; {{ lead_med_values[2] }}</td>
                            <td>&ge; {{ lead_mean_values[1] }} &amp; &lt; {{ lead_mean_values[2] }}</td>
                            <td>&ge; {{ lead_prcast_values[1] }} &amp; &lt; {{ lead_prcast_values[2] }}</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="pbsqu3"></span></td>
                            <td>&ge; {{ lead_med_values[2] }} &amp; &lt; {{ lead_med_values[3] }}</td>
                            <td>&ge; {{ lead_mean_values[2] }} &amp; &lt; {{ lead_mean_values[3] }}</td>
                            <td>&ge; {{ lead_prcast_values[2] }} &amp; &lt; {{ lead_prcast_values[3] }}</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="pbsqu4"></span></td>
                            <td>&ge; {{ lead_med_values[3] }}</td>
                            <td>&ge; {{ lead_mean_values[3] }}</td>
                            <td>&ge; {{ lead_prcast_values[3] }}</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="pbsqufill"></span></td>
                            <td>No Data {{ lead_med_values[0] }}</td>
                          </tr>
                        </q-markup-table>
                      </font>
                    </q-popup-proxy>
                  </q-btn>
                </td>
              </tr>
              <tr>
                <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">Manganese (ppb and %)</q-tooltip>
                <td>Manganese</td>
                <td><q-radio v-on:input="showMapPanelRadioLayer" val="ncwellwise_manganese_med" v-model="currentvariable" color="teal" /></td>
                <td><q-radio v-on:input="showMapPanelRadioLayer" val="ncwellwise_manganese_mean" v-model="currentvariable" color="teal" /></td>
                <td><q-radio v-on:input="showMapPanelRadioLayer" val="ncwellwise_manganese_prcast" v-model="currentvariable" color="teal" /></td>
                <td>
                  <q-btn flat dense round icon="fas fa-list" class="teal text-black" aria-label="Map Legend">
                    <q-tooltip>Click to View Map Legend</q-tooltip>
                    <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
                      <font size="2" face="Arial" >
                        <q-markup-table dense class="bg-teal-1">
                          <tr>
                            <td style="text-align:center;" colspan="2">Median (ppb)</td>
                            <td style="text-align:center;" >Mean (ppb)</td>
                            <td style="text-align:center;" >% Above Standard</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="mnsqu1"></span></td>
                            <td>&gt; {{ manganese_med_values[1] }}</td>
                            <td>&gt; {{ manganese_mean_values[1] }}</td>
                            <td>&gt; {{ manganese_prcast_values[1] }}</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="mnsqu2"></span></td>
                            <td>&ge; {{ manganese_med_values[1] }} &amp; &lt; {{ manganese_med_values[2] }}</td>
                            <td>&ge; {{ manganese_mean_values[1] }} &amp; &lt; {{ manganese_mean_values[2] }}</td>
                            <td>&ge; {{ manganese_prcast_values[1] }} &amp; &lt; {{ manganese_prcast_values[2] }}</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="mnsqu3"></span></td>
                            <td>&ge; {{ manganese_med_values[2] }} &amp; &lt; {{ manganese_med_values[3] }}</td>
                            <td>&ge; {{ manganese_mean_values[2] }} &amp; &lt; {{ manganese_mean_values[3] }}</td>
                            <td>&ge; {{ manganese_prcast_values[2] }} &amp; &lt; {{ manganese_prcast_values[3] }}</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="mnsqu4"></span></td>
                            <td>&ge; {{ manganese_med_values[3] }}</td>
                            <td>&ge; {{ manganese_mean_values[3] }}</td>
                            <td>&ge; {{ manganese_prcast_values[3] }}</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="squfill"></span></td>
                            <td>No Data {{ manganese_med_values[0] }}</td>
                          </tr>
                        </q-markup-table>
                      </font>
                    </q-popup-proxy>
                  </q-btn>
                </td>
              </tr>
            </table>
          </div>
        </q-expansion-item>
        <!-- // NC wellwise layers -->

        <!-- // ACS Census layers -->
        <q-expansion-item dense dense-toggle expand-separator icon="list" label="Sociodemographic Indicators, by Census Tracts">
          <div class="q-pa-md q-gutter-y-sm column">
            <table cellspacing="3" cellpadding="0" style="width:100%">
              <tr>
                <td>
                  <!-- // legend -->
                  Legend
                </td>
                <td>
                    <q-tooltip>Click to View Map Legend</q-tooltip>
                    <q-btn flat dense round icon="fas fa-list" class="teal text-black" aria-label="Map Legend">
                    <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
                      <font size="2" face="Arial" >
                        <q-markup-table dense class="bg-teal-1">
                          <tr>
                            <td style="padding:5px"><span class="acssqu1"></span></td>
                            <td>&gt; {{ census_acs_values[1] }}%</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="acssqu2"></span></td>
                            <td>&ge; {{ census_acs_values[1] }}% &amp; &lt; {{ census_acs_values[2] }}%</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="acssqu3"></span></td>
                            <td>&ge; {{ census_acs_values[2] }}% &amp; &lt; {{ census_acs_values[3] }}%</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="acssqu4"></span></td>
                            <td>&ge; {{ census_acs_values[3] }}%</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="squfill"></span></td>
                            <td>No Data {{ census_acs_values[0] }}</td>
                          </tr>
                        </q-markup-table>
                      </font>
                    </q-popup-proxy>
                    </q-btn>
                  <!-- // legend -->
                </td>
              </tr>
              <tr>
                <td>
                  <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                  <q-radio v-on:input="showMapPanelRadioLayer" val="percent_below_poverty_level" v-model="currentvariable" color="teal" />
                </td>
                <td>
                  Percent Below the Poverty Level
                </td>
              </tr>
              <tr>
                <td>
                  <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                  <q-radio v-on:input="showMapPanelRadioLayer" val="american_indian_and_alaska_native_alone" v-model="currentvariable" color="teal" />
                </td>
                <td>
                  Percent Native American
                </td>
              </tr>
              <tr>
                <td>
                  <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                  <q-radio v-on:input="showMapPanelRadioLayer" val="asian_alone" v-model="currentvariable" color="teal" />
                </td>
                <td>
                  Percent Asian
                </td>
              </tr>
              <tr>
                <td>
                  <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                  <q-radio v-on:input="showMapPanelRadioLayer" val="black_or_african_american_alone" v-model="currentvariable" color="teal" />
                </td>
                <td>
                  Percent Non-Hispanic Black
                </td>
              </tr>
              <tr>
                <td>
                  <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                  <q-radio v-on:input="showMapPanelRadioLayer" val="native_hawaiian_and_other_pacific_islander_alone" v-model="currentvariable" color="teal" />
                </td>
                <td>
                  Percent Non-Hispanic Native Hawaiian and other Pacific Islander
                </td>
              </tr>
              <tr>
                <td>
                  <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                  <q-radio v-on:input="showMapPanelRadioLayer" val="white_alone" v-model="currentvariable" color="teal" />
                </td>
                <td>
                  Percent Non-Hispanic White
                </td>
              </tr>
              <tr>
                <td>
                  <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                  <q-radio v-on:input="showMapPanelRadioLayer" val="two_or_more_races" v-model="currentvariable" color="teal" />
                </td>
                <td>
                  Percent Two or more Races
                </td>
              </tr>
              <tr>
              <td>
                  <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                  <q-radio v-on:input="showMapPanelRadioLayer" val="hispanic_or_latino_of_any_race" v-model="currentvariable" color="teal" />
                </td>
                <td>
                  Percent Hispanic
                </td>
              </tr>
                <tr>
                <td>
                  <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                  <q-radio v-on:input="showMapPanelRadioLayer" val="not_hispanic_or_latino" v-model="currentvariable" color="teal" />
                </td>
                <td>
                  Percent Non-Hispanic
                </td>
              </tr>
              <tr>
                <td>
                  <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                  <q-radio v-on:input="showMapPanelRadioLayer" val="speak_a_language_other_than_english" v-model="currentvariable" color="teal" />
                </td>
                <td>
                  Percent of Population, 5 Years and Over, who Speak a language other than English
                </td>
              </tr>
            </table>
          </div>
        </q-expansion-item>
        <!-- // ACS Census layers -->

        <!-- // EJScreen layers -->
        <!-- // d_ldpnt_2 -->
        <q-expansion-item dense dense-toggle expand-separator icon="list" label="Environmental Justice Indicators, by Census Block Group">
          <div class="q-pa-md q-gutter-y-sm column">
            <table cellspacing="0" cellpadding="0" style="width:100%">
              <tr>
                <td>
                  <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                  <q-radio v-on:input="showMapPanelRadioLayer" val="d_ldpnt_2" v-model="currentvariable" color="teal" />
                </td>
                <td>
                  EJ Index for % pre-1960 housing (lead paint indicator)
                </td>
                <td>
                  <!-- // d_ldpnt_2 -->
                    <q-btn flat dense round icon="fas fa-list" class="teal text-black" aria-label="Map Legend">
                      <q-tooltip>Click to View Map Legend</q-tooltip>
                      <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
                        <font size="2" face="Arial" >
                          <q-markup-table dense class="bg-teal-1">
                            <tr>
                              <td style="text-align:center;" colspan="2">Lead Paint</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="ejssqu1"></span></td>
                              <td>&gt; {{ d_ldpnt_2_values[1] }}</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="ejssqu2"></span></td>
                              <td>&ge; {{ d_ldpnt_2_values[1] }} &amp; &lt; {{ d_ldpnt_2_values[2] }}</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="ejssqu3"></span></td>
                              <td>&ge; {{ d_ldpnt_2_values[2] }} &amp; &lt; {{ d_ldpnt_2_values[3] }}</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="ejssqu4"></span></td>
                              <td>&ge; {{ d_ldpnt_2_values[3] }}</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="squfill"></span></td>
                              <td>No Data {{ d_ldpnt_2_values[0] }}</td>
                            </tr>
                          </q-markup-table>
                        </font>
                      </q-popup-proxy>
                    </q-btn>
                    <!-- // d_ldpnt_2_values legend -->
                </td>
              </tr>
              <tr>
                <td>
                  <!-- // d_dslpm_2 -->
                  <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                  <q-radio v-on:input="showMapPanelRadioLayer" val="d_dslpm_2" v-model="currentvariable" color="teal" />
                </td>
                <td>
                  EJ Index for Diesel particulate matter level in air
                  <!-- // d_dslpm_2 -->
                </td>
                <td>
                    <!-- // d_dslpm_2_values legend -->
                    <q-btn flat dense round icon="fas fa-list" class="teal text-black" aria-label="Map Legend">
                      <q-tooltip>Click to View Map Legend</q-tooltip>
                      <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
                        <font size="2" face="Arial" >
                          <q-markup-table dense class="bg-teal-1">
                            <tr>
                              <td style="text-align:center;" colspan="2">Diesel Particulate</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="ejssqu1"></span></td>
                              <td>&gt; {{ d_dslpm_2_values[1] }}</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="ejssqu2"></span></td>
                              <td>&ge; {{ d_dslpm_2_values[1] }} &amp; &lt; {{ d_dslpm_2_values[2] }}</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="ejssqu3"></span></td>
                              <td>&ge; {{ d_dslpm_2_values[2] }} &amp; &lt; {{ d_dslpm_2_values[3] }}</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="ejssqu4"></span></td>
                              <td>&ge; {{ d_dslpm_2_values[3] }}</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="squfill"></span></td>
                              <td>No Data {{ d_dslpm_2_values[0] }}</td>
                            </tr>
                          </q-markup-table>
                        </font>
                      </q-popup-proxy>
                    </q-btn>
                    <!-- // d_dslpm_2_values legend -->
                </td>
              </tr>
              <tr>
                <td>
                  <!-- // d_cancr_2 -->
                  <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                  <q-radio v-on:input="showMapPanelRadioLayer" val="d_cancr_2" v-model="currentvariable" color="teal" />
                </td>
                <td>
                  EJ Index for Air toxics cancer risk
                  <!-- // d_cancr_2 -->
                </td>
                <td>
                    <!-- // d_cancr_2_values legend -->
                    <q-btn flat dense round icon="fas fa-list" class="teal text-black" aria-label="Map Legend">
                      <q-tooltip>Click to View Map Legend</q-tooltip>
                      <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
                        <font size="2" face="Arial" >
                          <q-markup-table dense class="bg-teal-1">
                            <tr>
                              <td style="text-align:center;" colspan="2">Air Toxics Cancer</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="ejssqu1"></span></td>
                              <td>&gt; {{ d_cancr_2_values[1] }}</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="ejssqu2"></span></td>
                              <td>&ge; {{ d_cancr_2_values[1] }} &amp; &lt; {{ d_cancr_2_values[2] }}</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="ejssqu3"></span></td>
                              <td>&ge; {{ d_cancr_2_values[2] }} &amp; &lt; {{ d_cancr_2_values[3] }}</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="ejssqu4"></span></td>
                              <td>&ge; {{ d_cancr_2_values[3] }}</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="squfill"></span></td>
                              <td>No Data {{ d_cancr_2_values[0] }}</td>
                            </tr>
                          </q-markup-table>
                        </font>
                      </q-popup-proxy>
                    </q-btn>
                    <!-- // d_cancr_2_values legend -->
                </td>
              </tr>
              <tr>
                <td>
                  <!-- // d_resp_2 -->
                  <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                  <q-radio v-on:input="showMapPanelRadioLayer" val="d_resp_2" v-model="currentvariable" color="teal" />
                </td>
                <td>
                  EJ Index for Air toxics respiratory hazard index
                  <!-- // d_resp_2 -->
                </td>
                <td>
                    <!-- // d_resp_2_values legend -->
                    <q-btn flat dense round icon="fas fa-list" class="teal text-black" aria-label="Map Legend">
                      <q-tooltip>Click to View Map Legend</q-tooltip>
                      <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
                        <font size="2" face="Arial" >
                          <q-markup-table dense class="bg-teal-1">
                            <tr>
                              <td style="text-align:center;" colspan="2">Air toxics respiratory</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="ejssqu1"></span></td>
                              <td>&gt; {{ d_resp_2_values[1] }}</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="ejssqu2"></span></td>
                              <td>&ge; {{ d_resp_2_values[1] }} &amp; &lt; {{ d_resp_2_values[2] }}</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="ejssqu3"></span></td>
                              <td>&ge; {{ d_resp_2_values[2] }} &amp; &lt; {{ d_resp_2_values[3] }}</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="ejssqu4"></span></td>
                              <td>&ge; {{ d_resp_2_values[3] }}</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="squfill"></span></td>
                              <td>No Data {{ d_resp_2_values[0] }}</td>
                            </tr>
                          </q-markup-table>
                        </font>
                      </q-popup-proxy>
                    </q-btn>
                    <!-- // d_resp_2_values legend -->
                </td>
              </tr>
              <tr>
                <td>
                  <!-- // d_ptraf_2 -->
                    <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                    <q-radio v-on:input="showMapPanelRadioLayer" val="d_ptraf_2" v-model="currentvariable" color="teal" />
                  </td>
                  <td>
                      EJ Index for Traffic proximity and volume
                  <!-- // d_ptraf_2 -->
                </td>
                <td>
                    <!-- // d_ptraf_2_values legend -->
                    <q-btn flat dense round icon="fas fa-list" class="teal text-black" aria-label="Map Legend">
                      <q-tooltip>Click to View Map Legend</q-tooltip>
                      <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
                        <font size="2" face="Arial" >
                          <q-markup-table dense class="bg-teal-1">
                            <tr>
                              <td style="text-align:center;" colspan="2">Traffic</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="ejssqu1"></span></td>
                              <td>&gt; {{ d_ptraf_2_values[1] }}</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="ejssqu2"></span></td>
                              <td>&ge; {{ d_ptraf_2_values[1] }} &amp; &lt; {{ d_ptraf_2_values[2] }}</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="ejssqu3"></span></td>
                              <td>&ge; {{ d_ptraf_2_values[2] }} &amp; &lt; {{ d_ptraf_2_values[3] }}</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="ejssqu4"></span></td>
                              <td>&ge; {{ d_ptraf_2_values[3] }}</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="squfill"></span></td>
                              <td>No Data {{ d_ptraf_2_values[0] }}</td>
                            </tr>
                          </q-markup-table>
                        </font>
                      </q-popup-proxy>
                    </q-btn>
                    <!-- // d_ptraf_2_values legend -->
                </td>
              </tr>
              <tr>
                <td>
                  <!-- // d_pwdis_2 -->
                    <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                    <q-radio v-on:input="showMapPanelRadioLayer" val="d_pwdis_2" v-model="currentvariable" color="teal" />
                  </td>
                  <td>
                      EJ Index for Indicator for major direct dischargers to water
                  <!-- // d_pwdis_2 -->
                </td>
                <td>
                    <!-- // d_pwdis_2_values legend -->
                    <q-btn flat dense round icon="fas fa-list" class="teal text-black" aria-label="Map Legend">
                      <q-tooltip>Click to View Map Legend</q-tooltip>
                      <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
                        <font size="2" face="Arial" >
                          <q-markup-table dense class="bg-teal-1">
                            <tr>
                              <td style="text-align:center;" colspan="2">Direct Discharges</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="ejssqu1"></span></td>
                              <td>&gt; {{ d_pwdis_2_values[1] }}</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="ejssqu2"></span></td>
                              <td>&ge; {{ d_pwdis_2_values[1] }} &amp; &lt; {{ d_pwdis_2_values[2] }}</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="ejssqu3"></span></td>
                              <td>&ge; {{ d_pwdis_2_values[2] }} &amp; &lt; {{ d_pwdis_2_values[3] }}</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="ejssqu4"></span></td>
                              <td>&ge; {{ d_pwdis_2_values[3] }}</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="squfill"></span></td>
                              <td>No Data {{ d_pwdis_2_values[0] }}</td>
                            </tr>
                          </q-markup-table>
                        </font>
                      </q-popup-proxy>
                    </q-btn>
                    <!-- // d_pwdis_2_values legend -->
                </td>
              </tr>
              <tr>
                <td>
                  <!-- // d_pnpl_2 -->
                    <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                    <q-radio v-on:input="showMapPanelRadioLayer" val="d_pnpl_2" v-model="currentvariable" color="teal" />
                  </td>
                  <td>
                      EJ Index for Proximity to National Priorities List (NPL) sites
                  <!-- // d_pnpl_2 -->
                </td>
                <td>
                    <!-- // d_pnpl_2_values legend -->
                    <q-btn flat dense round icon="fas fa-list" class="teal text-black" aria-label="Map Legend">
                      <q-tooltip>Click to View Map Legend</q-tooltip>
                      <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
                        <font size="2" face="Arial" >
                          <q-markup-table dense class="bg-teal-1">
                            <tr>
                              <td style="text-align:center;" colspan="2">National Priorities</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="ejssqu1"></span></td>
                              <td>&gt; {{ d_pnpl_2_values[1] }}</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="ejssqu2"></span></td>
                              <td>&ge; {{ d_pnpl_2_values[1] }} &amp; &lt; {{ d_pnpl_2_values[2] }}</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="ejssqu3"></span></td>
                              <td>&ge; {{ d_pnpl_2_values[2] }} &amp; &lt; {{ d_pnpl_2_values[3] }}</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="ejssqu4"></span></td>
                              <td>&ge; {{ d_pnpl_2_values[3] }}</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="squfill"></span></td>
                              <td>No Data {{ d_pnpl_2_values[0] }}</td>
                            </tr>
                          </q-markup-table>
                        </font>
                      </q-popup-proxy>
                    </q-btn>
                    <!-- // d_pnpl_2_values legend -->
                </td>
              </tr>
              <tr>
                <td>
                  <!-- // d_prmp_2 -->
                  <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                  <q-radio v-on:input="showMapPanelRadioLayer" val="d_prmp_2" v-model="currentvariable" color="teal" />
                </td>
                <td>
                  EJ Index for Proximity to Risk Management Plan (RMP) facilities
                  <!-- // d_prmp_2 -->
                </td>
                <td>
                    <!-- // d_prmp_2_values legend -->
                    <q-btn flat dense round icon="fas fa-list" class="teal text-black" aria-label="Map Legend">
                      <q-tooltip>Click to View Map Legend</q-tooltip>
                      <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
                        <font size="2" face="Arial" >
                          <q-markup-table dense class="bg-teal-1">
                            <tr>
                              <td style="text-align:center;" colspan="2">Risk Management</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="ejssqu1"></span></td>
                              <td>&gt; {{ d_prmp_2_values[1] }}</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="ejssqu2"></span></td>
                              <td>&ge; {{ d_prmp_2_values[1] }} &amp; &lt; {{ d_prmp_2_values[2] }}</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="ejssqu3"></span></td>
                              <td>&ge; {{ d_prmp_2_values[2] }} &amp; &lt; {{ d_prmp_2_values[3] }}</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="ejssqu4"></span></td>
                              <td>&ge; {{ d_prmp_2_values[3] }}</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="squfill"></span></td>
                              <td>No Data {{ d_prmp_2_values[0] }}</td>
                            </tr>
                          </q-markup-table>
                        </font>
                      </q-popup-proxy>
                    </q-btn>
                    <!-- // d_prmp_2_values legend -->
                </td>
              </tr>
              <tr>
                <td>
                  <!-- // d_ptsdf_2 -->
                  <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                  <q-radio v-on:input="showMapPanelRadioLayer" val="d_ptsdf_2" v-model="currentvariable" color="teal" />
                </td>
                <td>
                  EJ Index for Proximity to Treatment Storage and Disposal (TSDF) facilities
                  <!-- // d_ptsdf_2 -->
                </td>
                <td>
                    <!-- // d_ptsdf_2_values legend -->
                    <q-btn flat dense round icon="fas fa-list" class="teal text-black" aria-label="Map Legend">
                      <q-tooltip>Click to View Map Legend</q-tooltip>
                      <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
                        <font size="2" face="Arial" >
                          <q-markup-table dense class="bg-teal-1">
                            <tr>
                              <td style="text-align:center;" colspan="2">Storage and Disposal</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="ejssqu1"></span></td>
                              <td>&gt; {{ d_ptsdf_2_values[1] }}</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="ejssqu2"></span></td>
                              <td>&ge; {{ d_ptsdf_2_values[1] }} &amp; &lt; {{ d_ptsdf_2_values[2] }}</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="ejssqu3"></span></td>
                              <td>&ge; {{ d_ptsdf_2_values[2] }} &amp; &lt; {{ d_ptsdf_2_values[3] }}</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="ejssqu4"></span></td>
                              <td>&ge; {{ d_ptsdf_2_values[3] }}</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="squfill"></span></td>
                              <td>No Data {{ d_ptsdf_2_values[0] }}</td>
                            </tr>
                          </q-markup-table>
                        </font>
                      </q-popup-proxy>
                    </q-btn>
                    <!-- // d_ptsdf_2_values legend -->
                </td>
              </tr>
              <tr>
                <td>
                  <!-- // d_ozone_2 -->
                  <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                  <q-radio v-on:input="showMapPanelRadioLayer" val="d_ozone_2" v-model="currentvariable" color="teal" />
                </td>
                <td>
                  EJ Index for Ozone level in air
                  <!-- // d_ozone_2 -->
                </td>
                <td>
                    <!-- // d_ozone_2_values legend -->
                    <q-btn flat dense round icon="fas fa-list" class="teal text-black" aria-label="Map Legend">
                      <q-tooltip>Click to View Map Legend</q-tooltip>
                      <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
                        <font size="2" face="Arial" >
                          <q-markup-table dense class="bg-teal-1">
                            <tr>
                              <td style="text-align:center;" colspan="2">Tropospheric Ozone</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="ejssqu1"></span></td>
                              <td>&gt; {{ d_ozone_2_values[1] }}</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="ejssqu2"></span></td>
                              <td>&ge; {{ d_ozone_2_values[1] }} &amp; &lt; {{ d_ozone_2_values[2] }}</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="ejssqu3"></span></td>
                              <td>&ge; {{ d_ozone_2_values[2] }} &amp; &lt; {{ d_ozone_2_values[3] }}</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="ejssqu4"></span></td>
                              <td>&ge; {{ d_ozone_2_values[3] }}</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="squfill"></span></td>
                              <td>No Data {{ d_ozone_2_values[0] }}</td>
                            </tr>
                          </q-markup-table>
                        </font>
                      </q-popup-proxy>
                    </q-btn>
                    <!-- // d_ozone_2_values legend -->
                </td>
              </tr>
              <tr>
                <td>
                  <!-- // d_pm25_2 -->
                  <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                  <q-radio v-on:input="showMapPanelRadioLayer" val="d_pm25_2" v-model="currentvariable" color="teal" />
                </td>
                <td>
                  EJ Index for PM2.5 level in air
                  <!-- // d_pm25_2 -->
                </td>
                <td>
                    <!-- // d_pm25_2_values legend -->
                    <q-btn flat dense round icon="fas fa-list" class="teal text-black" aria-label="Map Legend">
                      <q-tooltip>Click to View Map Legend</q-tooltip>
                      <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
                        <font size="2" face="Arial" >
                          <q-markup-table dense class="bg-teal-1">
                            <tr>
                              <td style="text-align:center;" colspan="2">PM2.5</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="ejssqu1"></span></td>
                              <td>&gt; {{ d_pm25_2_values[1] }}</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="ejssqu2"></span></td>
                              <td>&ge; {{ d_pm25_2_values[1] }} &amp; &lt; {{ d_pm25_2_values[2] }}</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="ejssqu3"></span></td>
                              <td>&ge; {{ d_pm25_2_values[2] }} &amp; &lt; {{ d_pm25_2_values[3] }}</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="ejssqu4"></span></td>
                              <td>&ge; {{ d_pm25_2_values[3] }}</td>
                            </tr>
                            <tr>
                              <td style="padding:5px"><span class="squfill"></span></td>
                              <td>No Data {{ d_pm25_2_values[0] }}</td>
                            </tr>
                          </q-markup-table>
                        </font>
                      </q-popup-proxy>
                    </q-btn>
                    <!-- // d_pm25_2_values legend -->
                </td>
              </tr>
            </table>
          </div>
        </q-expansion-item>
        <!-- // EJScreen layers -->

        <!-- // Health layers -->
        <q-expansion-item dense dense-toggle expand-separator icon="list" label="Health Outcomes, by Zip Code">
          <div class="q-pa-md q-gutter-y-sm column">
            <table cellspacing="3" cellpadding="0" style="width:100%">
              <tr>
                <!-- // legend -->
                <td>
                  Legend
                </td>
                <td>
                  <q-tooltip>Click to View Map Legend</q-tooltip>
                  <q-btn flat dense round icon="fas fa-list" class="teal text-black" aria-label="Map Legend">
                    <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
                      <font size="2" face="Arial" >
                        <q-markup-table dense class="bg-teal-1">
                          <tr>
                             <td style="text-align:center;" colspan="2">Total Cases</td>
                             <td style="text-align:center;" >Cases Per 10,000 Residents</td>
                             <td style="text-align:center;" >Cases Per 100,000 Residents</td>
                             <td style="text-align:center;" >Deaths</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="heasqu1"></span></td>
                            <td>&gt; {{ covid_cases_values[1] }}</td>
                            <td>&gt; {{ covid_cases_per_10000_res_values[1] }}</td>
                            <td>&gt; {{ covid_cases_per_100000_res_values[1] }}</td>
                            <td>&gt; {{ covid_deaths_values[1] }}</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="heasqu2"></span></td>
                            <td>&ge; {{ covid_cases_values[1] }} &amp; &lt; {{ covid_cases_values[2] }}</td>
                            <td>&ge; {{ covid_cases_per_10000_res_values[1] }} &amp; &lt; {{ covid_cases_per_10000_res_values[2] }}</td>
                            <td>&ge; {{ covid_cases_per_100000_res_values[1] }} &amp; &lt; {{ covid_cases_per_100000_res_values[2] }}</td>
                            <td>&ge; {{ covid_deaths_values[1] }} &amp; &lt; {{ covid_deaths_values[2] }}</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="heasqu3"></span></td>
                            <td>&ge; {{ covid_cases_values[2] }} &amp; &lt; {{ covid_cases_values[3] }}</td>
                            <td>&ge; {{ covid_cases_per_10000_res_values[2] }} &amp; &lt; {{ covid_cases_per_10000_res_values[3] }}</td>
                            <td>&ge; {{ covid_cases_per_100000_res_values[2] }} &amp; &lt; {{ covid_cases_per_100000_res_values[3] }}</td>
                            <td>&ge; {{ covid_deaths_values[2] }} &amp; &lt; {{ covid_deaths_values[3] }}</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="heasqu4"></span></td>
                            <td>&ge; {{ covid_cases_values[3] }} &amp; &lt; {{ covid_cases_values[3] }}</td>
                            <td>&ge; {{ covid_cases_per_10000_res_values[3] }} &amp; &lt; {{ covid_cases_per_10000_res_values[4] }}</td>
                            <td>&ge; {{ covid_cases_per_100000_res_values[3] }} &amp; &lt; {{ covid_cases_per_100000_res_values[4] }}</td>
                            <td>&ge; {{ covid_deaths_values[3] }} &amp; &lt; {{ covid_deaths_values[4] }}</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="heasqu5"></span></td>
                            <td>&ge; {{ covid_cases_values[4] }} &amp; &lt; {{ covid_cases_values[5] }}</td>
                            <td>&ge; {{ covid_cases_per_10000_res_values[4] }} &amp; &lt; {{ covid_cases_per_10000_res_values[5] }}</td>
                            <td>&ge; {{ covid_cases_per_100000_res_values[4] }} &amp; &lt; {{ covid_cases_per_100000_res_values[5] }}</td>
                            <td>&ge; {{ covid_deaths_values[4] }} &amp; &lt; {{ covid_deaths_values[5] }}</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="heasqu6"></span></td>
                              <td>&ge; {{ covid_cases_values[5] }}</td>
                              <td>&ge; {{ covid_cases_per_10000_res_values[5] }}</td>
                              <td>&ge; {{ covid_cases_per_100000_res_values[5] }}</td>
                              <td>&ge; {{ covid_deaths_values[5] }}</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="squfill"></span></td>
                            <td>No Data {{ covid_cases_values[0] }}</td>
                          </tr>
                        </q-markup-table>
                      </font>
                    </q-popup-proxy>
                  </q-btn>
                </td>
                <!-- // legend -->
              </tr>
              <tr>
                <td>
                  <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From North Carolina Department of Health and Human Services</q-tooltip>
                  <q-radio v-on:input="showMapPanelRadioLayer" val="cases" v-model="currentvariable" color="teal" />
                </td>
                <td>
                  <q-item-label>Covid-19 Total Cases</q-item-label>
                </td>
              </tr>
              <tr>
                <td>
                  <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From North Carolina Department of Health and Human Services</q-tooltip>
                  <q-radio v-on:input="showMapPanelRadioLayer" val="cases_per_10000_res" v-model="currentvariable" color="teal" />
                </td>
                <td>
                  <q-item-label>Covid-19 Cases Per 10,000 Residents</q-item-label>
                </td>
              </tr>
              <tr>
                <td>
                  <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From North Carolina Department of Health and Human Services</q-tooltip>
                  <q-radio v-on:input="showMapPanelRadioLayer" val="cases_per_100000_res" v-model="currentvariable" color="teal" />
                </td>
                <td>
                  <q-item-label>Covid-19 Cases Per 100,000 Residents-</q-item-label>
                </td>
              </tr>
              <tr>
                <td>
                  <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From North Carolina Department of Health and Human Services</q-tooltip>
                  <q-radio v-on:input="showMapPanelRadioLayer" val="deaths" v-model="currentvariable" color="teal" />
                </td>
                <td>
                  <q-item-label>Covid-19 Deaths</q-item-label>
                </td>
              </tr>
            </table>
           </div>
        </q-expansion-item>
        <!-- // Health layers -->

        <!-- // Additional Features -->
        <q-expansion-item dense dense-toggle expand-separator icon="list" label="Additional Features">
          <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From North Carolina One Map</q-tooltip>
          <div class="q-pa-md q-gutter-y-sm column">
            <q-toggle
              :label="`North Carolina County Boundaries${ ncCountiesModel }`"
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
      <q-btn flat dense round icon="fas fa-columns" class="bg-teal text-black" aria-label="Dual Screen Map" @click="$router.replace('/dual')">
        <q-tooltip>Go to Side by Side Screen Map</q-tooltip>
      </q-btn>
    </q-page-sticky>
    <q-page-sticky position="top-left" :offset="[18, 18]">
      <div v-if="!leftDrawerOpen">
        <q-btn flat dense round icon="fas fa-sign-out-alt" class="bg-teal text-black" @click="leftDrawerOpen = !leftDrawerOpen" aria-label="Menu">
          <q-tooltip>Open &amp; Close Side Drawer</q-tooltip>
        </q-btn>
      </div>
      <div v-else>
        <q-btn flat dense round icon="fas fa-sign-in-alt fa-rotate-180" class="bg-teal text-black" @click="leftDrawerOpen = !leftDrawerOpen" aria-label="Menu">
          <q-tooltip>Open &amp; Close Side Drawer</q-tooltip>
        </q-btn>
      </div>
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
      <div v-if="!rightDrawerOpen">
        <q-btn flat dense round icon="fas fa-sign-out-alt fa-rotate-180" class="bg-teal text-black" @click="rightDrawerOpen = !rightDrawerOpen" aria-label="Menu">
          <q-tooltip>Open &amp; Close Side Drawer</q-tooltip>
        </q-btn>
      </div>
      <div v-else>
        <q-btn flat dense round icon="fas fa-sign-in-alt" class="bg-teal text-black" @click="rightDrawerOpen = !rightDrawerOpen" aria-label="Menu">
          <q-tooltip>Open &amp; Close Side Drawer</q-tooltip>
        </q-btn>
      </div>
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
      <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">Map Location Tools</q-tooltip>
      <q-fab icon="keyboard_arrow_up" direction="up" label-position="left" external-label color="teal text-black" label="Map Location Tools">
        <q-fab-action color="teal" class="text-black" icon="fas fa-map-marked-alt" label-position="left" external-label label="Map an Address">
          <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
            <q-card class="bg-teal-1">
              <q-banner inline-actions class="bg-teal-1">
                <div class="q-pa-md" style="max-width: 400px">
                  <q-form @submit="address2Geoloc" @reset="resetAddress" class="q-gutter-md">
                    <q-input filled v-model="address" label="Address *" hint="Address, City, NC and USA or ZipCode USA" lazy-rules
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
        <q-fab-action color="teal" class="text-black" icon="fas fa-map-marked-alt" label-position="left" external-label label="Set Map to Your Current Location">
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
      arsncolors: ['rgba(91, 95, 99, 0.65)', 'rgba(247, 121, 237, 0.65)', 'rgba(194, 76, 237, 0.65)', 'rgba(165, 52, 235, 0.65)', 'rgba(127, 3, 252, 0.65)'],
      cadmcolors: ['rgba(91, 95, 99, 0.65)', 'rgba(223, 235, 52, 0.65)', 'rgba(235, 192, 52, 0.65)', 'rgba(235, 162, 52, 0.65)', 'rgba(235, 89, 52, 0.65)'],
      leadcolors: ['rgba(50, 110, 219, 0.65)', 'rgba(196, 200, 207, 0.65)', 'rgba(155, 158, 163, 0.65)', 'rgba(108, 112, 120, 0.65)', 'rgba(39, 40, 43, 0.65)'],
      mngncolors: ['rgba(91, 95, 99, 0.65)', 'rgba(194, 232, 190, 0.65)', 'rgba(81, 222, 67, 0.65)', 'rgba(25, 128, 11, 0.65)', 'rgba(14, 82, 5, 0.65)'],
      acscolors: ['rgba(91, 95, 99, 0.85)', 'rgba(252, 210, 211, 0.85)', 'rgba(247, 84, 90, 0.85)', 'rgba(212, 4, 9, 0.85)', 'rgba(122, 1, 5, 0.85)'],
      ejscolors: ['rgba(91, 95, 99, 0.65)', 'rgba(235, 252, 3, 0.65)', 'rgba(252, 186, 3, 0.65)', 'rgba(252, 128, 3, 0.65)', 'rgba(252, 82, 3, 0.65)'],
      covidcolors: ['rgba(91, 95, 99, 0.65)', 'rgba(34, 240, 219, 0.65)', 'rgba(34, 223, 240, 0.65)', 'rgba(34, 185, 240, 0.65)', 'rgba(22, 141, 245, 0.65)', 'rgba(22, 74, 245, 0.65)', 'rgba(23, 2, 247, 0.65)'],
      arsenic_med_values: [-999.99, 3.55, 6.847, 11.18],
      arsenic_mean_values: [-999.99, 3.549, 3.71, 4.47],
      arsenic_prcast_values: [-999.99, 0.1, 2.607, 9.187],
      cadmium_med_values: [-999.99, 0.72, 0.76, 0.80],
      cadmium_mean_values: [-999.99, 0.719, 0.73, 0.77],
      cadmium_prcast_values: [-999.99, 0.1, 0.993, 3.21],
      lead_med_values: [-999.99, 3.8, 5.77, 9.0],
      lead_mean_values: [-999.99, 3.548, 4.033, 4.977],
      lead_prcast_values: [-999.99, 0.35, 2.61, 5.66],
      manganese_med_values: [-999.99, 23.0, 40.0, 70.0],
      manganese_mean_values: [-999.99, 35.0, 55.0, 100.0],
      manganese_prcast_values: [-999.99, 5, 25, 45.0],
      census_acs_values: [-999.99, 25, 50, 75],
      d_ldpnt_2_values: [-99999.9999, -20.0, 0.0, 27.0],
      d_dslpm_2_values: [-99999.9999, -50.0, 0.0, 60.0],
      d_cancr_2_values: [-99999.9999, 2204.147, 7227.09, 7227.09],
      d_resp_2_values: [-99999.9999, -86.266, -14.005, 97.526],
      d_ptraf_2_values: [-99999.9999, 0.0, 8126.669, 74230.562],
      d_pwdis_2_values: [-99999.9999, -0.0000746, 0.0, 0.000039],
      d_pnpl_2_values: [-99999.9999, -8.798, 0.0, 8.0],
      d_prmp_2_values: [-99999.9999, -34.097, -3.503, 50.083],
      d_ptsdf_2_values: [-99999.9999, -61.175, -3.583, 126.669],
      d_ozone_2_values: [-99999.9999, 3418.589, 9484.232, 17558.825],
      d_pm25_2_values: [-99999.9999, -167.385, 1043.186, 2801.709],
      covid_cases_values: [-999.99, 1328, 2656, 3984, 5416, 6644],
      covid_cases_per_10000_res_values: [-999.99, 586.0, 1172.0, 1758.0, 2344.0, 2930.0],
      covid_cases_per_100000_res_values: [-999.99, 5859.0, 11718.0, 17577.0, 23436.0, 29295.0],
      covid_deaths_values: [-999.99, 17, 34, 51, 65, 85],
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
  computed: {
    arsenicColors () {
      return {
        '--arsenic-colors': this.arsncolors
      }
    },
    cadmiumColors () {
      return {
        '--cadmium-colors': this.cadmcolors
      }
    },
    leadColors () {
      return {
        '--lead-colors': this.leadcolors
      }
    },
    manganeseColors () {
      return {
        '--manganese-colors': this.mngncolors
      }
    },
    acsColors () {
      return {
        '--acs-colors': this.acscolors
      }
    },
    ejscreenColors () {
      return {
        '--ejscreen-colors': this.ejscolors
      }
    },
    covidColors () {
      return {
        '--covid-colors': this.covidcolors
      }
    }
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
        this.zoom = 10
      } else if (this.getlocation === 'False') {
        this.currentlocation = 'False'
        this.zoom = 8
        this.center = [-79.0193, 35.0]
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
          this.zoom = 10
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
    getColors: function (data, values, colors, variable, layer) {
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
      } else if (colors.length === 5) {
        if (layer === 'ncwelllayer') {
          if (data[variable.substring(11)] === values[0]) {
            this.varcolor = colors[0]
          } else if (data[variable.substring(11)] < values[1]) {
            this.varcolor = colors[1]
          } else if (data[variable.substring(11)] >= values[1] && data[variable.substring(11)] < values[2]) {
            this.varcolor = colors[2]
          } else if (data[variable.substring(11)] >= values[2] && data[variable.substring(11)] < values[3]) {
            this.varcolor = colors[3]
          } else if (data[variable.substring(11)] >= values[3]) {
            this.varcolor = colors[4]
          }
        } else {
          if (data[variable] === values[0]) {
            this.varcolor = colors[0]
          } else if (data[variable] < values[1]) {
            this.varcolor = colors[1]
          } else if (data[variable] >= values[1] && data[variable] < values[2]) {
            this.varcolor = colors[2]
          } else if (data[variable] >= values[2] && data[variable] < values[3]) {
            this.varcolor = colors[3]
          } else if (data[variable] >= values[3]) {
            this.varcolor = colors[4]
          }
        }
      }
    },
    getncwellwiseStyle: function () {
      return feature => {
        let selected = !!this.vtSelection[feature.get(this.vtIdProp)]
        let data = feature.getProperties()
        let variable = this.currentvariable
        if (this.currentvariable === 'ncwellwise_arsenic_med') {
          this.getColors(data, this.arsenic_med_values, this.arsncolors, variable, 'ncwelllayer')
        } else if (this.currentvariable === 'ncwellwise_arsenic_mean') {
          this.getColors(data, this.arsenic_mean_values, this.arsncolors, variable, 'ncwelllayer')
        } else if (this.currentvariable === 'ncwellwise_arsenic_prcast') {
          this.getColors(data, this.arsenic_prcast_values, this.arsncolors, variable, 'ncwelllayer')
        } else if (this.currentvariable === 'ncwellwise_cadmium_med') {
          this.getColors(data, this.cadmium_med_values, this.cadmcolors, variable, 'ncwelllayer')
        } else if (this.currentvariable === 'ncwellwise_cadmium_mean') {
          this.getColors(data, this.cadmium_mean_values, this.cadmcolors, variable, 'ncwelllayer')
        } else if (this.currentvariable === 'ncwellwise_cadmium_prcast') {
          this.getColors(data, this.cadmium_prcast_values, this.cadmcolors, variable, 'ncwelllayer')
        } else if (this.currentvariable === 'ncwellwise_lead_med') {
          this.getColors(data, this.lead_med_values, this.leadcolors, variable, 'ncwelllayer')
        } else if (this.currentvariable === 'ncwellwise_lead_mean') {
          this.getColors(data, this.lead_mean_values, this.leadcolors, variable, 'ncwelllayer')
        } else if (this.currentvariable === 'ncwellwise_lead_prcast') {
          this.getColors(data, this.lead_prcast_values, this.leadcolors, variable, 'ncwelllayer')
        } else if (this.currentvariable === 'ncwellwise_manganese_med') {
          this.getColors(data, this.manganese_med_values, this.mngncolors, variable, 'ncwelllayer')
        } else if (this.currentvariable === 'ncwellwise_manganese_mean') {
          this.getColors(data, this.manganese_mean_values, this.mngncolors, variable, 'ncwelllayer')
        } else if (this.currentvariable === 'ncwellwise_manganese_prcast') {
          this.getColors(data, this.manganese_prcast_values, this.mngncolors, variable, 'ncwelllayer')
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
      return feature => {
        let selected = !!this.vtSelection[feature.get(this.vtIdProp)]
        let data = feature.getProperties()
        let variable = this.currentvariable
        this.getColors(data, this.census_acs_values, this.acscolors, variable, 'acslayer')
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
      return feature => {
        let selected = !!this.vtSelection[feature.get(this.vtIdProp)]
        let data = feature.getProperties()
        let variable = this.currentvariable
        if (this.currentvariable === 'd_ldpnt_2') {
          this.getColors(data, this.d_ldpnt_2_values, this.ejscolors, variable, 'ejslayer')
        } else if (this.currentvariable === 'd_dslpm_2') {
          this.getColors(data, this.d_dslpm_2_values, this.ejscolors, variable, 'ejslayer')
        } else if (this.currentvariable === 'd_cancr_2') {
          this.getColors(data, this.d_cancr_2_values, this.ejscolors, variable, 'ejslayer')
        } else if (this.currentvariable === 'd_resp_2') {
          this.getColors(data, this.d_resp_2_values, this.ejscolors, variable, 'ejslayer')
        } else if (this.currentvariable === 'd_ptraf_2') {
          this.getColors(data, this.d_ptraf_2_values, this.ejscolors, variable, 'ejslayer')
        } else if (this.currentvariable === 'd_pwdis_2') {
          this.getColors(data, this.d_pwdis_2_values, this.ejscolors, variable, 'ejslayer')
        } else if (this.currentvariable === 'd_pnpl_2') {
          this.getColors(data, this.d_pnpl_2_values, this.ejscolors, variable, 'ejslayer')
        } else if (this.currentvariable === 'd_prmp_2') {
          this.getColors(data, this.d_prmp_2_values, this.ejscolors, variable, 'ejslayer')
        } else if (this.currentvariable === 'd_ptsdf_2') {
          this.getColors(data, this.d_ptsdf_2_values, this.ejscolors, variable, 'ejslayer')
        } else if (this.currentvariable === 'd_ozone_2') {
          this.getColors(data, this.d_ozone_2_values, this.ejscolors, variable, 'ejslayer')
        } else if (this.currentvariable === 'd_pm25_2') {
          this.getColors(data, this.d_pm25_2_values, this.ejscolors, variable, 'ejslayer')
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
      return feature => {
        let selected = !!this.vtSelection[feature.get(this.vtIdProp)]
        let data = feature.getProperties()
        let variable = this.currentvariable
        if (this.currentvariable === 'cases') {
          this.getColors(data, this.covid_cases_values, this.covidcolors, variable, 'covidlayer')
        } else if (this.currentvariable === 'cases_per_10000_res') {
          this.getColors(data, this.covid_cases_per_10000_res_values, this.covidcolors, variable, 'covidlayer')
        } else if (this.currentvariable === 'cases_per_100000_res') {
          this.getColors(data, this.covid_cases_per_100000_res_values, this.covidcolors, variable, 'covidlayer')
        } else if (this.currentvariable === 'deaths') {
          this.getColors(data, this.covid_deaths_values, this.covidcolors, variable, 'covidlayer')
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
            strokeWidth: (this.zoom / 2.0),
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
    background-color: rgba(247, 121, 237, 0.65);
    // background-color: var(--arsenic-colors[1]);
    display: inline-block;
  }
  .assqu2 {
    height: 15px;
    width: 15px;
    background-color: rgba(194, 76, 237, 0.65);
    // background-color: var(--arsenic-colors[2]);
    display: inline-block;
  }
  .assqu3 {
    height: 15px;
    width: 15px;
    background-color: rgba(165, 52, 235, 0.65);
    // background-color: var(--arsenic-colors[3]);
    display: inline-block;
  }
  .assqu4 {
    height: 15px;
    width: 15px;
    background-color: rgba(127, 3, 252, 0.65);
    // background-color: var(--arsenic-colors[4]);
    display: inline-block;
  }
  .cdsqu1 {
    height: 15px;
    width: 15px;
    background-color: rgba(223, 235, 52, 0.65);
    // background-color: var(--cadmium-colors[1]);
    display: inline-block;
  }
  .cdsqu2 {
    height: 15px;
    width: 15px;
    background-color: rgba(235, 192, 52, 0.65);
    // background-color: var(--cadmium-colors[2]);
    display: inline-block;
  }
  .cdsqu3 {
    height: 15px;
    width: 15px;
    background-color: rgba(235, 162, 52, 0.65);
    // background-color: var(--cadmium-colors[3]);
    display: inline-block;
  }
  .cdsqu4 {
    height: 15px;
    width: 15px;
    background-color: rgba(235, 89, 52, 0.65);
    // background-color: var(--cadmium-colors[4]);
    display: inline-block;
  }
  .pbsqu1 {
    height: 15px;
    width: 15px;
    background-color: rgba(196, 200, 207, 0.65);
    // background-color: var(--lead-colors[1]);
    display: inline-block;
  }
  .pbsqu2 {
    height: 15px;
    width: 15px;
    background-color: rgba(155, 158, 163, 0.65);
    // background-color: var(--lead-colors[2]);
    display: inline-block;
  }
  .pbsqu3 {
    height: 15px;
    width: 15px;
    background-color: rgba(108, 112, 120, 0.65);
    // background-color: var(--lead-colors[3]);
    display: inline-block;
  }
  .pbsqu4 {
    height: 15px;
    width: 15px;
    background-color: rgba(39, 40, 43, 0.65);
    // background-color: var(--lead-colors[4]);
    display: inline-block;
  }
  .mnsqu1 {
    height: 15px;
    width: 15px;
    background-color: rgba(194, 232, 190, 0.65);
    // background-color: var(--manganese-colors[1]);
    display: inline-block;
  }
  .mnsqu2 {
    height: 15px;
    width: 15px;
    background-color: rgba(81, 222, 67, 0.65);
    // background-color: var(--manganese-colors[2]);
    display: inline-block;
  }
  .mnsqu3 {
    height: 15px;
    width: 15px;
    background-color: rgba(25, 128, 11, 0.65);
    // background-color: var(--manganese-colors[3]);
    display: inline-block;
  }
  .mnsqu4 {
    height: 15px;
    width: 15px;
    background-color: rgba(14, 82, 5, 0.65);
    // background-color: var(--manganese-colors[4]);
    display: inline-block;
  }
  .acssqu1 {
    height: 15px;
    width: 15px;
    background-color: rgba(252, 210, 211, 0.85);
    // background-color: var(--acs-colors[1]);
    display: inline-block;
  }
  .acssqu2 {
    height: 15px;
    width: 15px;
    background-color: rgba(247, 84, 90, 0.85);
    // background-color: var(--acs-colors[2]);
    display: inline-block;
  }
  .acssqu3 {
    height: 15px;
    width: 15px;
    background-color: rgba(212, 4, 9, 0.85);
    // background-color: var(--acs-colors[3]);
    display: inline-block;
  }
  .acssqu4 {
    height: 15px;
    width: 15px;
    background-color: rgba(122, 1, 5, 0.85);
    // background-color: var(--acs-colors[4]);
    display: inline-block;
  }
  .heasqu1 {
    height: 15px;
    width: 15px;
    background-color: rgba(34, 240, 219, 0.65);
    // background-color: var(--covid-colors[1]);
    display: inline-block;
  }
  .heasqu2 {
    height: 15px;
    width: 15px;
    background-color: rgba(34, 223, 240, 0.65);
    // background-color: var(--covid-colors[2]);
    display: inline-block;
  }
  .heasqu3 {
    height: 15px;
    width: 15px;
    background-color: rgba(34, 185, 240, 0.65);
    // background-color: var(--covid-colors[3]);
    display: inline-block;
  }
  .heasqu4 {
    height: 15px;
    width: 15px;
    background-color: rgba(22, 141, 245, 0.65);
    // background-color: var(--covid-colors[4]);
    display: inline-block;
  }
  .heasqu5 {
    height: 15px;
    width: 15px;
    background-color: rgba(22, 74, 245, 0.65);
    // background-color: var(--covid-colors[5]);
    display: inline-block;
  }
  .heasqu6 {
    height: 15px;
    width: 15px;
    background-color: rgba(23, 2, 247, 0.65);
    // background-color: var(--covid-colors[6]);
    display: inline-block;
  }
  .ejssqu1 {
    height: 15px;
    width: 15px;
    background-color: rgba(235, 252, 3, 0.65);
    // background-color: var(--manganese-colors[1]);
    display: inline-block;
  }
  .ejssqu2 {
    height: 15px;
    width: 15px;
    background-color: rgba(252, 186, 3, 0.65);
    // background-color: var(--manganese-colors[2]);
    display: inline-block;
  }
  .ejssqu3 {
    height: 15px;
    width: 15px;
    background-color: rgba(252, 128, 3, 0.65);
    // background-color: var(--manganese-colors[3]);
    display: inline-block;
  }
  .ejssqu4 {
    height: 15px;
    width: 15px;
    background-color: rgba(252, 82, 3, 0.65);
    // background-color: var(--manganese-colors[4]);
    display: inline-block;
  }
  .q-input {
    height: 4.0em;
  }
  .q-select {
    height: 4.0em;
  }
</style>
