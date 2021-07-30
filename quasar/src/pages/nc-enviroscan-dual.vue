<template>
  <q-layout view="lhr lpr lfr">
    <!-- q-layout view="hhh lpl fff" -->
    <q-page-container>
      <q-header elevated class="bg-teal">
        <div class="row no-wrap shadow-1">
        <!-- // Map One Toolbar and Menu -->
        <q-toolbar class="col-4">
          <q-btn flat round dense icon="menu" class="q-mr-sm text-black">
            <q-tooltip>Map One Menu</q-tooltip>
            <q-menu content-class="bg-teal-1">
              <q-list dense style="min-width: 100px">
                <q-item clickable>
                  <q-item-section>Base Layers</q-item-section>
                  <q-item-section side>
                    <q-icon name="keyboard_arrow_right"></q-icon>
                  </q-item-section>

                  <q-menu anchor="top end" self="top start" content-class="bg-teal-1">
                    <q-list>
                      <q-item tag="label" v-ripple>
                        <q-radio v-on:input="showBaseLayer1" val="osm" v-model="baselayer1" color="teal" />
                        <q-item-section>
                          <q-item-label>OpenStreetMap</q-item-label>
                        </q-item-section>
                      </q-item>
                      <q-item tag="label" v-ripple>
                        <q-radio v-on:input="showBaseLayer1" val="mapbox" v-model="baselayer1" color="teal" />
                        <q-item-section>
                          <q-item-label>MapBox Satellite</q-item-label>
                        </q-item-section>
                      </q-item>
                    </q-list>
                  </q-menu>
                </q-item>
                <q-separator></q-separator>

                <q-item clickable>
                  <q-item-section>Clear Data</q-item-section>
                  <q-item-section side>
                    <q-icon name="keyboard_arrow_right"></q-icon>
                  </q-item-section>

                  <q-menu anchor="top end" self="top start" content-class="bg-teal-1">
                    <q-list>
                      <!-- // nolayer -->
                      <div class="q-pa-md" style="min-width: 200px">
                        <q-list link>
                          <q-item tag="label" v-ripple>
                            <q-radio v-on:input="showMap1PanelRadioLayer" val="nolayer1" v-model="currentradiovariable1" color="teal" />
                            <q-item-section>
                              <q-item-label>Clear Data</q-item-label>
                            </q-item-section>
                          </q-item>
                        </q-list>
                      </div>
                      <!-- // nolayer -->
                    </q-list>
                  </q-menu>
                </q-item>

                <q-separator></q-separator>
                <q-item clickable>
                  <q-item-section>Environmental Indicators, by Census Tracts</q-item-section>
                  <q-item-section side>
                    <q-icon name="keyboard_arrow_right"></q-icon>
                  </q-item-section>
                  <q-menu anchor="top end" self="top start" content-class="bg-teal-1">
                    <q-list>
                      <q-item dense tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">Select Map Style</q-tooltip>
                        <table cellspacing="1" cellpadding="1" style="width:100%">
                          <caption style="text-align:left">Select Map Style</caption>
                          <tr>
                            <td>No Interleave</td>
                            <td>Interleave One</td>
                            <td>Interleave Two</td>
                          </tr>
                          <tr>
                            <td><q-radio val="nopattern" v-model="ncwellmap1style" color="teal" /></td>
                            <td><q-radio val="pattern1" v-model="ncwellmap1style" color="teal" /></td>
                            <td><q-radio val="pattern2" v-model="ncwellmap1style" color="teal" /></td>
                          </tr>
                        </table>
                      </q-item>
                      <!-- // NC wellwise layers -->
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
                            <td><q-radio v-on:input="showMap1PanelRadioLayer" val="ncwellwise_arsenic_med" v-model="currentradiovariable1" color="teal" /></td>
                            <td><q-radio v-on:input="showMap1PanelRadioLayer" val="ncwellwise_arsenic_mean" v-model="currentradiovariable1" color="teal" /></td>
                            <td><q-radio v-on:input="showMap1PanelRadioLayer" val="ncwellwise_arsenic_prcast" v-model="currentradiovariable1" color="teal" /></td>
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
                                        <td>&lt; {{ arsenic_med_values[1] }}</td>
                                        <td>&lt; {{ arsenic_mean_values[1] }}</td>
                                        <td>&lt; {{ arsenic_prcast_values[1] }}</td>
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
                            <td><q-radio v-on:input="showMap1PanelRadioLayer" val="ncwellwise_cadmium_med" v-model="currentradiovariable1" color="teal" /></td>
                            <td><q-radio v-on:input="showMap1PanelRadioLayer" val="ncwellwise_cadmium_mean" v-model="currentradiovariable1" color="teal" /></td>
                            <td><q-radio v-on:input="showMap1PanelRadioLayer" val="ncwellwise_cadmium_prcast" v-model="currentradiovariable1" color="teal" /></td>
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
                                        <td>&lt; {{ cadmium_med_values[1] }}</td>
                                        <td>&lt; {{ cadmium_mean_values[1] }}</td>
                                        <td>&lt; {{ cadmium_prcast_values[1] }}</td>
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
                            <td><q-radio v-on:input="showMap1PanelRadioLayer" val="ncwellwise_lead_med" v-model="currentradiovariable1" color="teal" /></td>
                            <td><q-radio v-on:input="showMap1PanelRadioLayer" val="ncwellwise_lead_mean" v-model="currentradiovariable1" color="teal" /></td>
                            <td><q-radio v-on:input="showMap1PanelRadioLayer" val="ncwellwise_lead_prcast" v-model="currentradiovariable1" color="teal" /></td>
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
                                        <td>&lt; {{ lead_med_values[1] }}</td>
                                        <td>&lt; {{ lead_mean_values[1] }}</td>
                                        <td>&lt; {{ lead_prcast_values[1] }}</td>
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
                            <td><q-radio v-on:input="showMap1PanelRadioLayer" val="ncwellwise_manganese_med" v-model="currentradiovariable1" color="teal" /></td>
                            <td><q-radio v-on:input="showMap1PanelRadioLayer" val="ncwellwise_manganese_mean" v-model="currentradiovariable1" color="teal" /></td>
                            <td><q-radio v-on:input="showMap1PanelRadioLayer" val="ncwellwise_manganese_prcast" v-model="currentradiovariable1" color="teal" /></td>
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
                                        <td>&lt; {{ manganese_med_values[1] }}</td>
                                        <td>&lt; {{ manganese_mean_values[1] }}</td>
                                        <td>&lt; {{ manganese_prcast_values[1] }}</td>
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
                      <!-- // NC wellwise layers -->
                    </q-list>
                  </q-menu>
                </q-item>
                <q-item clickable>
                  <q-item-section>Sociodemographic Indicators, by Census Tracts</q-item-section>
                  <q-item-section side>
                    <q-icon name="keyboard_arrow_right"></q-icon>
                  </q-item-section>

                  <q-menu anchor="top end" self="top start" content-class="bg-teal-1">
                    <q-list>
                      <q-item dense tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">Select Map Style</q-tooltip>
                        <table cellspacing="1" cellpadding="1" style="width:100%">
                          <caption style="text-align:left">Select Map Style</caption>
                          <tr>
                            <td>No Interleave</td>
                            <td>Interleave One</td>
                            <td>Interleave Two</td>
                          </tr>
                          <tr>
                            <td><q-radio val="nopattern" v-model="acsmap1style" color="teal" /></td>
                            <td><q-radio val="pattern1" v-model="acsmap1style" color="teal" /></td>
                            <td><q-radio val="pattern2" v-model="acsmap1style" color="teal" /></td>
                          </tr>
                        </table>
                      </q-item>
                      <!-- // ACS Census layers -->
                      <div class="q-pa-md q-gutter-y-sm column">
                        <table cellspacing="3" cellpadding="3" style="width:100%">
                          <tr>
                            <td>
                              <!-- // legend -->
                              <q-tooltip>Click to View Map Legend</q-tooltip>
                              Legend   <q-btn flat dense round icon="fas fa-list" class="teal text-black" aria-label="Map Legend">
                                <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
                                  <font size="2" face="Arial" >
                                    <q-markup-table dense class="bg-teal-1">
                                      <tr>
                                        <td style="padding:5px"><span class="acssqu1"></span></td>
                                        <td>&lt; {{ census_acs_values[1] }}%</td>
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
                              <q-toggle
                                :label="`Percent Below the Poverty Level ${ povertyModel1 }`"
                                v-on:input="showMap1PanelToggleLayer('percent_below_poverty_level')"
                                color="teal"
                                false-value="Not Selected"
                                true-value="Selected"
                                v-model="povertyModel1"
                              >
                                <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                              </q-toggle>
                            </td>
                          </tr>
                          <tr>
                            <td>
                              <q-toggle
                                :label="`Percent Native American ${ nativeModel1 }`"
                                v-on:input="showMap1PanelToggleLayer('american_indian_and_alaska_native_alone')"
                                color="teal"
                                false-value="Not Selected"
                                true-value="Selected"
                                v-model="nativeModel1"
                              >
                                <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                              </q-toggle>
                            </td>
                          </tr>
                          <tr>
                            <td>
                              <q-toggle
                                :label="`Percent Asian ${ asianModel1 }`"
                                v-on:input="showMap1PanelToggleLayer('asian_alone')"
                                color="teal"
                                false-value="Not Selected"
                                true-value="Selected"
                                v-model="asianModel1"
                              >
                                <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                              </q-toggle>
                            </td>
                          </tr>
                          <tr>
                            <td>
                              <q-toggle
                                :label="`Percent Non-Hispanic Black ${ blackModel1 }`"
                                v-on:input="showMap1PanelToggleLayer('black_or_african_american_alone')"
                                color="teal"
                                false-value="Not Selected"
                                true-value="Selected"
                                v-model="blackModel1"
                              >
                                <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                              </q-toggle>
                            </td>
                          </tr>
                          <tr>
                            <td>
                              <q-toggle
                                :label="`Percent Non-Hispanic Native Hawaiian and other Pacific Islander ${ polyModel1 }`"
                                v-on:input="showMap1PanelToggleLayer('native_hawaiian_and_other_pacific_islander_alone')"
                                color="teal"
                                false-value="Not Selected"
                                true-value="Selected"
                                v-model="polyModel1"
                              >
                                <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                              </q-toggle>
                            </td>
                          </tr>
                          <tr>
                            <td>
                              <q-toggle
                                :label="`Percent Non-Hispanic White ${ whiteModel1 }`"
                                v-on:input="showMap1PanelToggleLayer('white_alone')"
                                color="teal"
                                false-value="Not Selected"
                                true-value="Selected"
                                v-model="whiteModel1"
                              >
                                <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                              </q-toggle>
                            </td>
                          </tr>
                          <tr>
                            <td>
                              <q-toggle
                                :label="`Percent Two or more Races ${ tworacesModel1 }`"
                                v-on:input="showMap1PanelToggleLayer('two_or_more_races')"
                                color="teal"
                                false-value="Not Selected"
                                true-value="Selected"
                                v-model="tworacesModel1"
                              >
                                <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                              </q-toggle>
                            </td>
                          </tr>
                          <tr>
                            <td>
                              <q-toggle
                                :label="`Percent Hispanic ${ hispModel1 }`"
                                v-on:input="showMap1PanelToggleLayer('hispanic_or_latino_of_any_race')"
                                color="teal"
                                false-value="Not Selected"
                                true-value="Selected"
                                v-model="hispModel1"
                              >
                                <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                              </q-toggle>
                            </td>
                          </tr>
                          <tr>
                            <td>
                              <q-toggle
                                :label="`Percent Non-Hispanic ${ nothispModel1 }`"
                                v-on:input="showMap1PanelToggleLayer('not_hispanic_or_latino')"
                                color="teal"
                                false-value="Not Selected"
                                true-value="Selected"
                                v-model="nothispModel1"
                              >
                                <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                              </q-toggle>
                            </td>
                          </tr>
                          <tr>
                            <td>
                              <q-toggle
                                :label="`Percent of Population, 5 Years and Over, who Speak a language other than English ${ langModel1 }`"
                                v-on:input="showMap1PanelToggleLayer('speak_a_language_other_than_english')"
                                color="teal"
                                false-value="Not Selected"
                                true-value="Selected"
                                v-model="langModel1"
                              >
                                <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                              </q-toggle>
                            </td>
                          </tr>
                        </table>
                      </div>
                      <!-- // ACS Census layers -->
                    </q-list>
                  </q-menu>
                </q-item>
                <q-item clickable>
                  <q-item-section>Environmental Justice Indicators, by Census Block Group</q-item-section>
                  <q-item-section side>
                    <q-icon name="keyboard_arrow_right"></q-icon>
                  </q-item-section>

                  <q-menu anchor="top end" self="top start" content-class="bg-teal-1">
                    <q-list>
                      <q-item dense tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">Select Map Style</q-tooltip>
                        <table cellspacing="1" cellpadding="1" style="width:100%">
                          <caption style="text-align:left">Select Map Style</caption>
                          <tr>
                            <td>No Interleave</td>
                            <td>Interleave One</td>
                            <td>Interleave Two</td>
                          </tr>
                          <tr>
                            <td><q-radio val="nopattern" v-model="ejsmap1style" color="teal" /></td>
                            <td><q-radio val="pattern1" v-model="ejsmap1style" color="teal" /></td>
                            <td><q-radio val="pattern2" v-model="ejsmap1style" color="teal" /></td>
                          </tr>
                        </table>
                      </q-item>
                      <!-- // EJScreen layers -->
                      <!-- // d_ldpnt_2 -->
                      <div class="q-pa-md q-gutter-y-sm column">
                        <table cellspacing="0" cellpadding="0" style="width:100%">
                          <tr>
                            <td>
                              <q-toggle
                                :label="`EJ Index for % pre-1960 housing (lead paint indicator) ${ d_ldpnt_2Model1 }`"
                                v-on:input="showMap1PanelToggleLayer('d_ldpnt_2')"
                                color="teal"
                                false-value="Not Selected"
                                true-value="Selected"
                                v-model="d_ldpnt_2Model1"
                              >
                                <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                              </q-toggle>
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
                                          <td>&lt; {{ d_ldpnt_2_values[1] }}</td>
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
                              <q-toggle
                                :label="`EJ Index for Diesel particulate matter level in air ${ d_dslpm_2Model1 }`"
                                v-on:input="showMap1PanelToggleLayer('d_dslpm_2')"
                                color="teal"
                                false-value="Not Selected"
                                true-value="Selected"
                                v-model="d_dslpm_2Model1"
                              >
                                <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                              </q-toggle>
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
                                          <td>&lt; {{ d_dslpm_2_values[1] }}</td>
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
                              <q-toggle
                                :label="`EJ Index for Air toxics cancer risk ${ d_cancr_2Model1 }`"
                                v-on:input="showMap1PanelToggleLayer('d_cancr_2')"
                                color="teal"
                                false-value="Not Selected"
                                true-value="Selected"
                                v-model="d_cancr_2Model1"
                              >
                                <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                              </q-toggle>
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
                                          <td>&lt; {{ d_cancr_2_values[1] }}</td>
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
                              <q-toggle
                                :label="`EJ Index for Air toxics respiratory hazard index ${ d_resp_2Model1 }`"
                                v-on:input="showMap1PanelToggleLayer('d_resp_2')"
                                color="teal"
                                false-value="Not Selected"
                                true-value="Selected"
                                v-model="d_resp_2Model1"
                              >
                                <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                              </q-toggle>
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
                                          <td>&lt; {{ d_resp_2_values[1] }}</td>
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
                              <q-toggle
                                :label="`EJ Index for Traffic proximity and volume ${ d_ptraf_2Model1 }`"
                                v-on:input="showMap1PanelToggleLayer('d_ptraf_2')"
                                color="teal"
                                false-value="Not Selected"
                                true-value="Selected"
                                v-model="d_ptraf_2Model1"
                              >
                                <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                              </q-toggle>
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
                                          <td>&lt; {{ d_ptraf_2_values[1] }}</td>
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
                              <q-toggle
                                :label="`EJ Index for Indicator for major direct dischargers to water ${ d_pwdis_2Model1 }`"
                                v-on:input="showMap1PanelToggleLayer('d_pwdis_2')"
                                color="teal"
                                false-value="Not Selected"
                                true-value="Selected"
                                v-model="d_pwdis_2Model1"
                              >
                                <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                              </q-toggle>
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
                                          <td>&lt; {{ d_pwdis_2_values[1] }}</td>
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
                              <q-toggle
                                :label="`EJ Index for Proximity to National Priorities List (NPL) sites ${ d_pnpl_2Model1 }`"
                                v-on:input="showMap1PanelToggleLayer('d_pnpl_2')"
                                color="teal"
                                false-value="Not Selected"
                                true-value="Selected"
                                v-model="d_pnpl_2Model1"
                              >
                                <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                              </q-toggle>
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
                                          <td>&lt; {{ d_pnpl_2_values[1] }}</td>
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
                              <q-toggle
                                :label="`EJ Index for Proximity to Risk Management Plan (RMP) facilities ${ d_prmp_2Model1 }`"
                                v-on:input="showMap1PanelToggleLayer('d_prmp_2')"
                                color="teal"
                                false-value="Not Selected"
                                true-value="Selected"
                                v-model="d_prmp_2Model1"
                              >
                                <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                              </q-toggle>
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
                                          <td>&lt; {{ d_prmp_2_values[1] }}</td>
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
                              <q-toggle
                                :label="`EJ Index for Proximity to Treatment Storage and Disposal (TSDF) facilities ${ d_ptsdf_2Model1 }`"
                                v-on:input="showMap1PanelToggleLayer('d_ptsdf_2')"
                                color="teal"
                                false-value="Not Selected"
                                true-value="Selected"
                                v-model="d_ptsdf_2Model1"
                              >
                                <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                              </q-toggle>
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
                                          <td>&lt; {{ d_ptsdf_2_values[1] }}</td>
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
                              <q-toggle
                                :label="`EJ Index for Ozone level in air ${ d_ozone_2Model1 }`"
                                v-on:input="showMap1PanelToggleLayer('d_ozone_2')"
                                color="teal"
                                false-value="Not Selected"
                                true-value="Selected"
                                v-model="d_ozone_2Model1"
                              >
                                <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                              </q-toggle>
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
                                          <td>&lt; {{ d_ozone_2_values[1] }}</td>
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
                              <q-toggle
                                :label="`EJ Index for PM2.5 level in air ${ d_pm25_2Model1 }`"
                                v-on:input="showMap1PanelToggleLayer('d_pm25_2')"
                                color="teal"
                                false-value="Not Selected"
                                true-value="Selected"
                                v-model="d_pm25_2Model1"
                              >
                                <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                              </q-toggle>
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
                                          <td>&lt; {{ d_pm25_2_values[1] }}</td>
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
                      <!-- // EJScreen layers -->
                    </q-list>
                  </q-menu>
                </q-item>

                <!-- // Health layers -->
                <q-item clickable>
                  <q-item-section>Health Outcomes</q-item-section>
                  <q-item-section side>
                    <q-icon name="keyboard_arrow_right"></q-icon>
                  </q-item-section>
                  <q-menu anchor="top end" self="top start" content-class="bg-teal-1">
                    <q-list>
                      <q-item clickable>
                        <q-item-section>Covide-19, by Zip Code</q-item-section>
                        <q-item-section side>
                          <q-icon name="keyboard_arrow_right"></q-icon>
                        </q-item-section>
                        <q-menu anchor="top end" self="top start" content-class="bg-teal-1">
                          <q-list>
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
                                              <td>&lt; {{ covid_cases_values[1] }}</td>
                                              <td>&lt; {{ covid_cases_per_10000_res_values[1] }}</td>
                                              <td>&lt; {{ covid_cases_per_100000_res_values[1] }}</td>
                                              <td>&lt; {{ covid_deaths_values[1] }}</td>
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
                                    <q-radio v-on:input="showMap1PanelRadioLayer" val="cases" v-model="currentradiovariable1" color="teal" />
                                  </td>
                                  <td>
                                    <q-item-label>Covid-19 Total Cases</q-item-label>
                                  </td>
                                </tr>
                                <tr>
                                  <td>
                                    <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From North Carolina Department of Health and Human Services</q-tooltip>
                                    <q-radio v-on:input="showMap1PanelRadioLayer" val="cases_per_10000_res" v-model="currentradiovariable1" color="teal" />
                                  </td>
                                  <td>
                                    <q-item-label>Covid-19 Cases Per 10,000 Residents</q-item-label>
                                  </td>
                                </tr>
                                <tr>
                                  <td>
                                    <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From North Carolina Department of Health and Human Services</q-tooltip>
                                    <q-radio v-on:input="showMap1PanelRadioLayer" val="cases_per_100000_res" v-model="currentradiovariable1" color="teal" />
                                  </td>
                                  <td>
                                    <q-item-label>Covid-19 Cases Per 100,000 Residents-</q-item-label>
                                  </td>
                                </tr>
                                <tr>
                                  <td>
                                    <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From North Carolina Department of Health and Human Services</q-tooltip>
                                    <q-radio v-on:input="showMap1PanelRadioLayer" val="deaths" v-model="currentradiovariable1" color="teal" />
                                  </td>
                                  <td>
                                    <q-item-label>Covid-19 Deaths</q-item-label>
                                  </td>
                                </tr>
                              </table>
                            </div>
                          </q-list>
                        </q-menu>
                      </q-item>
                      <q-item clickable>
                        <q-item-section>Births, by Census Tracts</q-item-section>
                        <q-item-section side>
                          <q-icon name="keyboard_arrow_right"></q-icon>
                        </q-item-section>
                        <q-menu anchor="top end" self="top start" content-class="bg-teal-1">
                          <q-list>
                            <div class="q-pa-md q-gutter-y-sm column">
                              <table cellspacing="3" cellpadding="0" style="width:100%">
                                <q-item dense tag="label" v-ripple>
                                  <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">Select Map Style</q-tooltip>
                                  <table cellspacing="1" cellpadding="1" style="width:100%">
                                    <caption style="text-align:left">Select Map Style</caption>
                                    <tr>
                                      <td>No Interleave</td>
                                      <td>Interleave One</td>
                                      <td>Interleave Two</td>
                                    </tr>
                                    <tr>
                                      <td><q-radio val="nopattern" v-model="pretermmap1style" color="teal" /></td>
                                      <td><q-radio val="pattern1" v-model="pretermmap1style" color="teal" /></td>
                                      <td><q-radio val="pattern2" v-model="pretermmap1style" color="teal" /></td>
                                    </tr>
                                  </table>
                                </q-item>
                                <tr>
                                  <!-- // legend -->
                                  <table cellspacing="3" cellpadding="0" style="width:100%">
                                    <tr>
                                      <td>
                                        Gestational age at delivery Legend
                                      </td>
                                      <td>
                                        <q-tooltip>Click to View Map Legend</q-tooltip>
                                        <q-btn flat dense round icon="fas fa-list" class="teal text-black" aria-label="Map Legend">
                                          <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
                                            <font size="2" face="Arial" >
                                              <q-markup-table dense class="bg-teal-1">
                                                <tr>
                                                   <td style="text-align:center;" colspan="2">mean of gestational age at delivery </td>
                                                </tr>
                                                <tr>
                                                  <td style="padding:5px"><span class="pretsqu1"></span></td>
                                                  <td>&lt; {{ ega_mean_avg_values[1] }}</td>
                                                </tr>
                                                <tr>
                                                  <td style="padding:5px"><span class="pretsqu2"></span></td>
                                                  <td>&ge; {{ ega_mean_avg_values[1] }} &amp; &lt; {{ ega_mean_avg_values[2] }}</td>
                                                </tr>
                                                <tr>
                                                  <td style="padding:5px"><span class="pretsqu3"></span></td>
                                                  <td>&ge; {{ ega_mean_avg_values[2] }} &amp; &lt; {{ ega_mean_avg_values[3] }}</td>
                                                </tr>
                                                <tr>
                                                  <td style="padding:5px"><span class="pretsqu4"></span></td>
                                                    <td>&ge; {{ ega_mean_avg_values[3] }}</td>
                                                </tr>
                                                <tr>
                                                  <td style="padding:5px"><span class="squfill"></span></td>
                                                  <td>No Data {{ ega_mean_avg_values[0] }}</td>
                                                </tr>
                                              </q-markup-table>
                                            </font>
                                          </q-popup-proxy>
                                        </q-btn>
                                      </td>
                                    </tr>
                                  </table>
                                  <!-- // legend -->
                                </tr>
                                <tr>
                                  <td>
                                    <q-toggle
                                      :label="`mean of gestational age calculated from last menstrual period (LMP) full cohort ${ fc_calcega_mean_avgModel1 }`"
                                      v-on:input="showMap1PanelToggleLayer('fc_calcega_mean_avg')"
                                      color="teal"
                                      false-value="Not Selected"
                                      true-value="Selected"
                                      v-model="fc_calcega_mean_avgModel1"
                                    >
                                      <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">Arithmetic mean of gestational age calculated from last menstrual period (LMP) for full cohort</q-tooltip>
                                    </q-toggle>
                                  </td>
                                </tr>
                                <tr>
                                  <td>
                                    <q-toggle
                                      :label="`mean of gestational age based on clinical estimate full cohorts ${ fc_clinega_mean_avgModel1 }`"
                                      v-on:input="showMap1PanelToggleLayer('fc_clinega_mean_avg')"
                                      color="teal"
                                      false-value="Not Selected"
                                      true-value="Selected"
                                      v-model="fc_clinega_mean_avgModel1"
                                    >
                                      <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">Arithmetic mean of gestational age based on clinical estimate for full cohort</q-tooltip>
                                    </q-toggle>
                                  </td>
                                </tr>
                                <tr>
                                  <td>
                                    <q-toggle
                                      :label="`mean of gestational age calculated from last menstrual period (LMP) singleton cohort ${ sc_calcega_mean_avgModel1 }`"
                                      v-on:input="showMap1PanelToggleLayer('sc_calcega_mean_avg')"
                                      color="teal"
                                      false-value="Not Selected"
                                      true-value="Selected"
                                      v-model="sc_calcega_mean_avgModel1"
                                    >
                                      <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">arithmetic mean of gestational age calculated from last menstrual period (LMP) for singleton cohort</q-tooltip>
                                    </q-toggle>
                                  </td>
                                </tr>
                                <tr>
                                  <td>
                                    <q-toggle
                                      :label="`mean of gestational age based on clinical estimate singleton cohorts ${ sc_clinega_mean_avgModel1 }`"
                                      v-on:input="showMap1PanelToggleLayer('sc_clinega_mean_avg')"
                                      color="teal"
                                      false-value="Not Selected"
                                      true-value="Selected"
                                      v-model="sc_clinega_mean_avgModel1"
                                    >
                                      <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">Arithmetic mean of gestational age based on clinical estimate for singleton cohort</q-tooltip>
                                    </q-toggle>
                                  </td>
                                </tr>
                                <tr>
                                  <table cellspacing="3" cellpadding="0" style="width:100%">
                                    <tr>
                                      <!-- // legend -->
                                      <td>
                                        Preterm births Legend
                                      </td>
                                      <td>
                                        <q-tooltip>Click to View Map Legend</q-tooltip>
                                        <q-btn flat dense round icon="fas fa-list" class="teal text-black" aria-label="Map Legend">
                                          <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
                                            <font size="2" face="Arial" >
                                              <q-markup-table dense class="bg-teal-1">
                                                <tr>
                                                   <td style="text-align:center;" colspan="2">Percent preterm births</td>
                                                </tr>
                                                <tr>
                                                  <td style="padding:5px"><span class="pretsqu1"></span></td>
                                                  <td>&lt; {{ preterm_percentage_values[1] }}</td>
                                                </tr>
                                                <tr>
                                                  <td style="padding:5px"><span class="pretsqu2"></span></td>
                                                  <td>&ge; {{ preterm_percentage_values[1] }} &amp; &lt; {{ preterm_percentage_values[2] }}</td>
                                                </tr>
                                                <tr>
                                                  <td style="padding:5px"><span class="pretsqu3"></span></td>
                                                  <td>&ge; {{ preterm_percentage_values[2] }} &amp; &lt; {{ preterm_percentage_values[3] }}</td>
                                                </tr>
                                                <tr>
                                                  <td style="padding:5px"><span class="pretsqu4"></span></td>
                                                    <td>&ge; {{ preterm_percentage_values[3] }}</td>
                                                </tr>
                                                <tr>
                                                  <td style="padding:5px"><span class="squfill"></span></td>
                                                  <td>No Data {{ preterm_percentage_values[0] }}</td>
                                                </tr>
                                              </q-markup-table>
                                            </font>
                                          </q-popup-proxy>
                                        </q-btn>
                                      </td>
                                      <!-- // legend -->
                                    </tr>
                                  </table>
                                </tr>
                                <tr>
                                  <td>
                                    <q-toggle
                                      :label="`percent preterm births, calculated from last menstrual period (LMP) for full cohort ${ fc_calcpreterm_percentageModel1 }`"
                                      v-on:input="showMap1PanelToggleLayer('fc_calcpreterm_percentage')"
                                      color="teal"
                                      false-value="Not Selected"
                                      true-value="Selected"
                                      v-model="fc_calcpreterm_percentageModel1"
                                    >
                                      <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">percentage of all observations with complete data that are preterm births, where preterm birth status is derived from gestational age calculated from last menstrual period (LMP) for full cohort</q-tooltip>
                                    </q-toggle>
                                  </td>
                                </tr>
                                <tr>
                                  <td>
                                    <q-toggle
                                      :label="`percent preterm births, based on clinical estimate full cohorts ${ fc_clinpreterm_percentageModel1 }`"
                                      v-on:input="showMap1PanelToggleLayer('fc_clinpreterm_percentage')"
                                      color="teal"
                                      false-value="Not Selected"
                                      true-value="Selected"
                                      v-model="fc_clinpreterm_percentageModel1"
                                    >
                                      <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">percentage of all observations with complete data that are preterm births, where preterm birth status is based on clinical estimate for full cohort</q-tooltip>
                                    </q-toggle>
                                  </td>
                                </tr>
                                <tr>
                                  <td>
                                    <q-toggle
                                      :label="`percent preterm births, calculated from last menstrual period (LMP) singleton cohort ${ sc_calcpreterm_percentageModel1 }`"
                                      v-on:input="showMap1PanelToggleLayer('sc_calcpreterm_percentage')"
                                      color="teal"
                                      false-value="Not Selected"
                                      true-value="Selected"
                                      v-model="sc_calcpreterm_percentageModel1"
                                    >
                                      <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">percentage of all observations with complete data that are preterm births, where preterm birth status is derived from gestational age calculated from last menstrual period (LMP) for singleton cohort</q-tooltip>
                                    </q-toggle>
                                  </td>
                                </tr>
                                <tr>
                                  <td>
                                    <q-toggle
                                      :label="`percent preterm births, based on clinical estimate singleton cohorts ${ sc_clinpreterm_percentageModel1 }`"
                                      v-on:input="showMap1PanelToggleLayer('sc_clinpreterm_percentage')"
                                      color="teal"
                                      false-value="Not Selected"
                                      true-value="Selected"
                                      v-model="sc_clinpreterm_percentageModel1"
                                    >
                                      <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">percentage of all observations with complete data that are preterm births, where preterm birth status is based on clinical estimate singleton cohort</q-tooltip>
                                    </q-toggle>
                                  </td>
                                </tr>
                              </table>
                            </div>
                          </q-list>
                        </q-menu>
                      </q-item>
                    </q-list>
                  </q-menu>
                </q-item>
                <!-- // Health layers -->

                <q-item clickable>
                  <q-item-section>Additional Features</q-item-section>
                  <q-item-section side>
                    <q-icon name="keyboard_arrow_right"></q-icon>
                  </q-item-section>

                  <q-menu anchor="top end" self="top start" content-class="bg-teal-1">
                    <q-list>
                      <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From North Carolina One Map</q-tooltip>
                      <div class="q-pa-md q-gutter-y-sm column">
                        <q-toggle
                          :label="`North Carolina County Boundaries ${ ncCountiesModel1 }`"
                          v-on:input="showMap1PanelToggleLayer('nccounties')"
                          color="teal"
                          false-value="Not Selected"
                          true-value="Selected"
                          v-model="ncCountiesModel1"
                        />
                      </div>
                    </q-list>
                  </q-menu>
                </q-item>
                <q-separator></q-separator>
                <q-item clickable v-close-popup>
                  <q-item-section>Close</q-item-section>
                </q-item>
              </q-list>
            </q-menu>
          </q-btn>
          <q-toolbar-title class="text-black">NC-Enviroscan Dual Map One</q-toolbar-title>
        </q-toolbar>
        <!-- // Map One Toolbar and Menu -->

        <!-- // Map Two Toolbar and Menu -->
        <q-toolbar class="col-7 text-black">
          <q-space />
          <q-btn flat round dense icon="menu" class="q-mr-sm text-black">
            <q-tooltip>Map Two Menu</q-tooltip>
            <q-menu content-class="bg-teal-1">
              <q-list dense style="min-width: 100px">
                <q-item clickable>
                  <q-item-section>Base Layers</q-item-section>
                  <q-item-section side>
                    <q-icon name="keyboard_arrow_right"></q-icon>
                  </q-item-section>

                  <q-menu anchor="top end" self="top start" content-class="bg-teal-1">
                    <q-list>
                      <q-item tag="label" v-ripple>
                        <q-radio v-on:input="showBaseLayer2" val="osm" v-model="baselayer2" color="teal" />
                        <q-item-section>
                          <q-item-label>OpenStreetMap</q-item-label>
                        </q-item-section>
                      </q-item>
                      <q-item tag="label" v-ripple>
                        <q-radio v-on:input="showBaseLayer2" val="mapbox" v-model="baselayer2" color="teal" />
                        <q-item-section>
                          <q-item-label>MapBox Satellite</q-item-label>
                        </q-item-section>
                      </q-item>
                    </q-list>
                  </q-menu>
                </q-item>
                <q-separator></q-separator>

                <q-item clickable>
                  <q-item-section>Clear Data</q-item-section>
                  <q-item-section side>
                    <q-icon name="keyboard_arrow_right"></q-icon>
                  </q-item-section>

                  <q-menu anchor="top end" self="top start" content-class="bg-teal-1">
                    <q-list>
                      <!-- // nolayer -->
                      <div class="q-pa-md" style="min-width: 200px">
                        <q-list link>
                          <q-item tag="label" v-ripple>
                            <q-radio v-on:input="showMap2PanelRadioLayer" val="nolayer2" v-model="currentradiovariable2" color="teal" />
                            <q-item-section>
                              <q-item-label>Clear Data</q-item-label>
                            </q-item-section>
                          </q-item>
                        </q-list>
                      </div>
                      <!-- // nolayer -->
                    </q-list>
                  </q-menu>
                </q-item>

                <q-separator></q-separator>
                <q-item clickable>
                  <q-item-section>Environmental Indicators, by Census Tracts</q-item-section>
                  <q-item-section side>
                    <q-icon name="keyboard_arrow_right"></q-icon>
                  </q-item-section>
                  <q-menu anchor="top end" self="top start" content-class="bg-teal-1">
                    <q-list>
                      <q-item dense tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">Select Map Style</q-tooltip>
                        <table cellspacing="1" cellpadding="1" style="width:100%">
                          <caption style="text-align:left">Select Map Style</caption>
                          <tr>
                            <td>No Interleave</td>
                            <td>Interleave One</td>
                            <td>Interleave Two</td>
                          </tr>
                          <tr>
                            <td><q-radio val="nopattern" v-model="ncwellmap2style" color="teal" /></td>
                            <td><q-radio val="pattern1" v-model="ncwellmap2style" color="teal" /></td>
                            <td><q-radio val="pattern2" v-model="ncwellmap2style" color="teal" /></td>
                          </tr>
                        </table>
                      </q-item>
                      <!-- // NC wellwise layers -->
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
                            <td><q-radio v-on:input="showMap2PanelRadioLayer" val="ncwellwise_arsenic_med" v-model="currentradiovariable2" color="teal" /></td>
                            <td><q-radio v-on:input="showMap2PanelRadioLayer" val="ncwellwise_arsenic_mean" v-model="currentradiovariable2" color="teal" /></td>
                            <td><q-radio v-on:input="showMap2PanelRadioLayer" val="ncwellwise_arsenic_prcast" v-model="currentradiovariable2" color="teal" /></td>
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
                                        <td>&lt; {{ arsenic_med_values[1] }}</td>
                                        <td>&lt; {{ arsenic_mean_values[1] }}</td>
                                        <td>&lt; {{ arsenic_prcast_values[1] }}</td>
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
                            <td><q-radio v-on:input="showMap2PanelRadioLayer" val="ncwellwise_cadmium_med" v-model="currentradiovariable2" color="teal" /></td>
                            <td><q-radio v-on:input="showMap2PanelRadioLayer" val="ncwellwise_cadmium_mean" v-model="currentradiovariable2" color="teal" /></td>
                            <td><q-radio v-on:input="showMap2PanelRadioLayer" val="ncwellwise_cadmium_prcast" v-model="currentradiovariable2" color="teal" /></td>
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
                                        <td>&lt; {{ cadmium_med_values[1] }}</td>
                                        <td>&lt; {{ cadmium_mean_values[1] }}</td>
                                        <td>&lt; {{ cadmium_prcast_values[1] }}</td>
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
                            <td><q-radio v-on:input="showMap2PanelRadioLayer" val="ncwellwise_lead_med" v-model="currentradiovariable2" color="teal" /></td>
                            <td><q-radio v-on:input="showMap2PanelRadioLayer" val="ncwellwise_lead_mean" v-model="currentradiovariable2" color="teal" /></td>
                            <td><q-radio v-on:input="showMap2PanelRadioLayer" val="ncwellwise_lead_prcast" v-model="currentradiovariable2" color="teal" /></td>
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
                                        <td>&lt; {{ lead_med_values[1] }}</td>
                                        <td>&lt; {{ lead_mean_values[1] }}</td>
                                        <td>&lt; {{ lead_prcast_values[1] }}</td>
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
                            <td><q-radio v-on:input="showMap2PanelRadioLayer" val="ncwellwise_manganese_med" v-model="currentradiovariable2" color="teal" /></td>
                            <td><q-radio v-on:input="showMap2PanelRadioLayer" val="ncwellwise_manganese_mean" v-model="currentradiovariable2" color="teal" /></td>
                            <td><q-radio v-on:input="showMap2PanelRadioLayer" val="ncwellwise_manganese_prcast" v-model="currentradiovariable2" color="teal" /></td>
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
                                        <td>&lt; {{ manganese_med_values[1] }}</td>
                                        <td>&lt; {{ manganese_mean_values[1] }}</td>
                                        <td>&lt; {{ manganese_prcast_values[1] }}</td>
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
                      <!-- // NC wellwise layers -->
                    </q-list>
                  </q-menu>
                </q-item>
                <q-item clickable>
                  <q-item-section>Sociodemographic Indicators, by Census Tracts</q-item-section>
                  <q-item-section side>
                    <q-icon name="keyboard_arrow_right"></q-icon>
                  </q-item-section>

                  <q-menu anchor="top end" self="top start" content-class="bg-teal-1">
                    <q-list>
                      <q-item dense tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">Select Map Style</q-tooltip>
                        <table cellspacing="1" cellpadding="1" style="width:100%">
                          <caption style="text-align:left">Select Map Style</caption>
                          <tr>
                            <td>No Interleave</td>
                            <td>Interleave One</td>
                            <td>Interleave Two</td>
                          </tr>
                          <tr>
                            <td><q-radio val="nopattern" v-model="acsmap2style" color="teal" /></td>
                            <td><q-radio val="pattern1" v-model="acsmap2style" color="teal" /></td>
                            <td><q-radio val="pattern2" v-model="acsmap2style" color="teal" /></td>
                          </tr>
                        </table>
                      </q-item>
                      <!-- // ACS Census layers -->
                      <div class="q-pa-md q-gutter-y-sm column">
                        <table cellspacing="3" cellpadding="3" style="width:100%">
                          <tr>
                            <!-- // legend -->
                            <td>
                              <q-tooltip>Click to View Map Legend</q-tooltip>
                              Legend   <q-btn flat dense round icon="fas fa-list" class="teal text-black" aria-label="Map Legend">
                                <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
                                  <font size="2" face="Arial" >
                                    <q-markup-table dense class="bg-teal-1">
                                      <tr>
                                        <td style="padding:5px"><span class="acssqu1"></span></td>
                                        <td>&lt; {{ census_acs_values[1] }}%</td>
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
                              <q-toggle
                                :label="`Percent Below the Poverty Level ${ povertyModel2 }`"
                                v-on:input="showMap2PanelToggleLayer('percent_below_poverty_level')"
                                color="teal"
                                false-value="Not Selected"
                                true-value="Selected"
                                v-model="povertyModel2"
                              >
                                <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                              </q-toggle>
                            </td>
                          </tr>
                          <tr>
                            <td>
                              <q-toggle
                                :label="`Percent Native American ${ nativeModel2 }`"
                                v-on:input="showMap2PanelToggleLayer('american_indian_and_alaska_native_alone')"
                                color="teal"
                                false-value="Not Selected"
                                true-value="Selected"
                                v-model="nativeModel2"
                              >
                                <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                              </q-toggle>
                            </td>
                          </tr>
                          <tr>
                            <td>
                              <q-toggle
                                :label="`Percent Asian ${ asianModel2 }`"
                                v-on:input="showMap2PanelToggleLayer('asian_alone')"
                                color="teal"
                                false-value="Not Selected"
                                true-value="Selected"
                                v-model="asianModel2"
                              >
                                <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                              </q-toggle>
                            </td>
                          </tr>
                          <tr>
                            <td>
                              <q-toggle
                                :label="`Percent Non-Hispanic Black ${ blackModel2 }`"
                                v-on:input="showMap2PanelToggleLayer('black_or_african_american_alone')"
                                color="teal"
                                false-value="Not Selected"
                                true-value="Selected"
                                v-model="blackModel2"
                              >
                                <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                              </q-toggle>
                            </td>
                          </tr>
                          <tr>
                            <td>
                              <q-toggle
                                :label="`Percent Non-Hispanic Native Hawaiian and other Pacific Islander ${ polyModel2 }`"
                                v-on:input="showMap2PanelToggleLayer('native_hawaiian_and_other_pacific_islander_alone')"
                                color="teal"
                                false-value="Not Selected"
                                true-value="Selected"
                                v-model="polyModel2"
                              >
                                <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                              </q-toggle>
                            </td>
                          </tr>
                          <tr>
                            <td>
                              <q-toggle
                                :label="`Percent Non-Hispanic White ${ whiteModel2 }`"
                                v-on:input="showMap2PanelToggleLayer('white_alone')"
                                color="teal"
                                false-value="Not Selected"
                                true-value="Selected"
                                v-model="whiteModel2"
                              >
                                <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                              </q-toggle>
                            </td>
                          </tr>
                          <tr>
                            <td>
                              <q-toggle
                                :label="`Percent Two or more Races ${ tworacesModel2 }`"
                                v-on:input="showMap2PanelToggleLayer('two_or_more_races')"
                                color="teal"
                                false-value="Not Selected"
                                true-value="Selected"
                                v-model="tworacesModel2"
                              >
                                <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                              </q-toggle>
                            </td>
                          </tr>
                          <tr>
                            <td>
                              <q-toggle
                                :label="`Percent Hispanic ${ hispModel2 }`"
                                v-on:input="showMap2PanelToggleLayer('hispanic_or_latino_of_any_race')"
                                color="teal"
                                false-value="Not Selected"
                                true-value="Selected"
                                v-model="hispModel2"
                              >
                                <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                              </q-toggle>
                            </td>
                          </tr>
                          <tr>
                            <td>
                              <q-toggle
                                :label="`Percent Non-Hispanic ${ nothispModel2 }`"
                                v-on:input="showMap2PanelToggleLayer('not_hispanic_or_latino')"
                                color="teal"
                                false-value="Not Selected"
                                true-value="Selected"
                                v-model="nothispModel2"
                              >
                                <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                              </q-toggle>
                            </td>
                          </tr>
                          <tr>
                            <td>
                              <q-toggle
                                :label="`Percent of Population, 5 Years and Over, who Speak a language other than English ${ langModel2 }`"
                                v-on:input="showMap2PanelToggleLayer('speak_a_language_other_than_english')"
                                color="teal"
                                false-value="Not Selected"
                                true-value="Selected"
                                v-model="langModel2"
                              >
                                <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                              </q-toggle>
                            </td>
                          </tr>
                        </table>
                      </div>
                      <!-- // ACS Census layers -->
                    </q-list>
                  </q-menu>
                </q-item>
                <q-item clickable>
                  <q-item-section>Environmental Justice Indicators, by Census Block Group</q-item-section>
                  <q-item-section side>
                    <q-icon name="keyboard_arrow_right"></q-icon>
                  </q-item-section>

                  <q-menu anchor="top end" self="top start" content-class="bg-teal-1">
                    <q-list>
                      <q-item dense tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">Select Map Style</q-tooltip>
                        <table cellspacing="1" cellpadding="1" style="width:100%">
                          <caption style="text-align:left">Select Map Style</caption>
                          <tr>
                            <td>No Interleave</td>
                            <td>Interleave One</td>
                            <td>Interleave Two</td>
                          </tr>
                          <tr>
                            <td><q-radio val="nopattern" v-model="ejsmap2style" color="teal" /></td>
                            <td><q-radio val="pattern1" v-model="ejsmap2style" color="teal" /></td>
                            <td><q-radio val="pattern2" v-model="ejsmap2style" color="teal" /></td>
                          </tr>
                        </table>
                      </q-item>
                      <!-- // EJScreen layers -->
                      <!-- // d_ldpnt_2 -->
                      <div class="q-pa-md q-gutter-y-sm column">
                        <table cellspacing="0" cellpadding="0" style="width:100%">
                          <tr>
                            <td>
                              <q-toggle
                                :label="`EJ Index for % pre-1960 housing (lead paint indicator) ${ d_ldpnt_2Model2 }`"
                                v-on:input="showMap2PanelToggleLayer('d_ldpnt_2')"
                                color="teal"
                                false-value="Not Selected"
                                true-value="Selected"
                                v-model="d_ldpnt_2Model2"
                              >
                                <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                              </q-toggle>
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
                                          <td>&lt; {{ d_ldpnt_2_values[1] }}</td>
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
                              <q-toggle
                                :label="`EJ Index for Diesel particulate matter level in air ${ d_dslpm_2Model2 }`"
                                v-on:input="showMap2PanelToggleLayer('d_dslpm_2')"
                                color="teal"
                                false-value="Not Selected"
                                true-value="Selected"
                                v-model="d_dslpm_2Model2"
                              >
                                <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                              </q-toggle>
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
                                          <td>&lt; {{ d_dslpm_2_values[1] }}</td>
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
                              <q-toggle
                                :label="`EJ Index for Air toxics cancer risk ${ d_cancr_2Model2 }`"
                                v-on:input="showMap2PanelToggleLayer('d_cancr_2')"
                                color="teal"
                                false-value="Not Selected"
                                true-value="Selected"
                                v-model="d_cancr_2Model2"
                              >
                                <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                              </q-toggle>
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
                                          <td>&lt; {{ d_cancr_2_values[1] }}</td>
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
                              <q-toggle
                                :label="`EJ Index for Air toxics respiratory hazard index ${ d_resp_2Model2 }`"
                                v-on:input="showMap2PanelToggleLayer('d_resp_2')"
                                color="teal"
                                false-value="Not Selected"
                                true-value="Selected"
                                v-model="d_resp_2Model2"
                              >
                                <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                              </q-toggle>
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
                                          <td>&lt; {{ d_resp_2_values[1] }}</td>
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
                              <q-toggle
                                :label="`EJ Index for Traffic proximity and volume ${ d_ptraf_2Model2 }`"
                                v-on:input="showMap2PanelToggleLayer('d_ptraf_2')"
                                color="teal"
                                false-value="Not Selected"
                                true-value="Selected"
                                v-model="d_ptraf_2Model2"
                              >
                                <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                              </q-toggle>
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
                                          <td>&lt; {{ d_ptraf_2_values[1] }}</td>
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
                              <q-toggle
                                :label="`EJ Index for Indicator for major direct dischargers to water ${ d_pwdis_2Model2 }`"
                                v-on:input="showMap2PanelToggleLayer('d_pwdis_2')"
                                color="teal"
                                false-value="Not Selected"
                                true-value="Selected"
                                v-model="d_pwdis_2Model2"
                              >
                                <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                              </q-toggle>
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
                                          <td>&lt; {{ d_pwdis_2_values[1] }}</td>
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
                              <q-toggle
                                :label="`EJ Index for Proximity to National Priorities List (NPL) sites ${ d_pnpl_2Model2 }`"
                                v-on:input="showMap2PanelToggleLayer('d_pnpl_2')"
                                color="teal"
                                false-value="Not Selected"
                                true-value="Selected"
                                v-model="d_pnpl_2Model2"
                              >
                                <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                              </q-toggle>
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
                                          <td>&lt; {{ d_pnpl_2_values[1] }}</td>
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
                              <q-toggle
                                :label="`EJ Index for Proximity to Risk Management Plan (RMP) facilities ${ d_prmp_2Model2 }`"
                                v-on:input="showMap2PanelToggleLayer('d_prmp_2')"
                                color="teal"
                                false-value="Not Selected"
                                true-value="Selected"
                                v-model="d_prmp_2Model2"
                              >
                                <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                              </q-toggle>
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
                                          <td>&lt; {{ d_prmp_2_values[1] }}</td>
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
                              <q-toggle
                                :label="`EJ Index for Proximity to Treatment Storage and Disposal (TSDF) facilities ${ d_ptsdf_2Model2 }`"
                                v-on:input="showMap2PanelToggleLayer('d_ptsdf_2')"
                                color="teal"
                                false-value="Not Selected"
                                true-value="Selected"
                                v-model="d_ptsdf_2Model2"
                              >
                                <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                              </q-toggle>
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
                                          <td>&lt; {{ d_ptsdf_2_values[1] }}</td>
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
                              <q-toggle
                                :label="`EJ Index for Ozone level in air ${ d_ozone_2Model2 }`"
                                v-on:input="showMap2PanelToggleLayer('d_ozone_2')"
                                color="teal"
                                false-value="Not Selected"
                                true-value="Selected"
                                v-model="d_ozone_2Model2"
                              >
                                <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                              </q-toggle>
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
                                          <td>&lt; {{ d_ozone_2_values[1] }}</td>
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
                              <q-toggle
                                :label="`EJ Index for PM2.5 level in air ${ d_pm25_2Model2 }`"
                                v-on:input="showMap2PanelToggleLayer('d_pm25_2')"
                                color="teal"
                                false-value="Not Selected"
                                true-value="Selected"
                                v-model="d_pm25_2Model2"
                              >
                                <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                              </q-toggle>
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
                                          <td>&lt; {{ d_pm25_2_values[1] }}</td>
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
                      <!-- // EJScreen layers -->
                    </q-list>
                  </q-menu>
                </q-item>

                <!-- // Health layers -->
                <q-item clickable>
                  <q-item-section>Health Outcomes</q-item-section>
                  <q-item-section side>
                    <q-icon name="keyboard_arrow_right"></q-icon>
                  </q-item-section>
                  <q-menu anchor="top end" self="top start" content-class="bg-teal-1">
                    <q-list>
                      <q-item clickable>
                        <q-item-section>Covide-19, by Zip Code</q-item-section>
                        <q-item-section side>
                          <q-icon name="keyboard_arrow_right"></q-icon>
                        </q-item-section>
                        <q-menu anchor="top end" self="top start" content-class="bg-teal-1">
                          <q-list>
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
                                              <td>&lt; {{ covid_cases_values[1] }}</td>
                                              <td>&lt; {{ covid_cases_per_10000_res_values[1] }}</td>
                                              <td>&lt; {{ covid_cases_per_100000_res_values[1] }}</td>
                                              <td>&lt; {{ covid_deaths_values[1] }}</td>
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
                                    <q-radio v-on:input="showMap2PanelRadioLayer" val="cases" v-model="currentradiovariable2" color="teal" />
                                  </td>
                                  <td>
                                    <q-item-label>Covid-19 Total Cases</q-item-label>
                                  </td>
                                </tr>
                                <tr>
                                  <td>
                                    <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From North Carolina Department of Health and Human Services</q-tooltip>
                                    <q-radio v-on:input="showMap2PanelRadioLayer" val="cases_per_10000_res" v-model="currentradiovariable2" color="teal" />
                                  </td>
                                  <td>
                                    <q-item-label>Covid-19 Cases Per 10,000 Residents</q-item-label>
                                  </td>
                                </tr>
                                <tr>
                                  <td>
                                    <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From North Carolina Department of Health and Human Services</q-tooltip>
                                    <q-radio v-on:input="showMap2PanelRadioLayer" val="cases_per_100000_res" v-model="currentradiovariable2" color="teal" />
                                  </td>
                                  <td>
                                    <q-item-label>Covid-19 Cases Per 100,000 Residents-</q-item-label>
                                  </td>
                                </tr>
                                <tr>
                                  <td>
                                    <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From North Carolina Department of Health and Human Services</q-tooltip>
                                    <q-radio v-on:input="showMap2PanelRadioLayer" val="deaths" v-model="currentradiovariable2" color="teal" />
                                  </td>
                                  <td>
                                    <q-item-label>Covid-19 Deaths</q-item-label>
                                  </td>
                                </tr>
                              </table>
                            </div>
                          </q-list>
                        </q-menu>
                      </q-item>
                      <q-item clickable>
                        <q-item-section>Births, by Census Tracts</q-item-section>
                        <q-item-section side>
                          <q-icon name="keyboard_arrow_right"></q-icon>
                        </q-item-section>
                        <q-menu anchor="top end" self="top start" content-class="bg-teal-1">
                          <q-list>
                            <div class="q-pa-md q-gutter-y-sm column">
                              <table cellspacing="3" cellpadding="0" style="width:100%">
                                <q-item dense tag="label" v-ripple>
                                  <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">Select Map Style</q-tooltip>
                                  <table cellspacing="1" cellpadding="1" style="width:100%">
                                    <caption style="text-align:left">Select Map Style</caption>
                                    <tr>
                                      <td>No Interleave</td>
                                      <td>Interleave One</td>
                                      <td>Interleave Two</td>
                                    </tr>
                                    <tr>
                                      <td><q-radio val="nopattern" v-model="pretermmap2style" color="teal" /></td>
                                      <td><q-radio val="pattern1" v-model="pretermmap2style" color="teal" /></td>
                                      <td><q-radio val="pattern2" v-model="pretermmap2style" color="teal" /></td>
                                    </tr>
                                  </table>
                                </q-item>
                                <tr>
                                  <!-- // legend -->
                                  <table cellspacing="3" cellpadding="0" style="width:100%">
                                    <tr>
                                      <td>
                                        Gestational age at delivery Legend
                                      </td>
                                      <td>
                                        <q-tooltip>Click to View Map Legend</q-tooltip>
                                        <q-btn flat dense round icon="fas fa-list" class="teal text-black" aria-label="Map Legend">
                                          <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
                                            <font size="2" face="Arial" >
                                              <q-markup-table dense class="bg-teal-1">
                                                <tr>
                                                   <td style="text-align:center;" colspan="2">mean of gestational age at delivery </td>
                                                </tr>
                                                <tr>
                                                  <td style="padding:5px"><span class="pretsqu1"></span></td>
                                                  <td>&lt; {{ ega_mean_avg_values[1] }}</td>
                                                </tr>
                                                <tr>
                                                  <td style="padding:5px"><span class="pretsqu2"></span></td>
                                                  <td>&ge; {{ ega_mean_avg_values[1] }} &amp; &lt; {{ ega_mean_avg_values[2] }}</td>
                                                </tr>
                                                <tr>
                                                  <td style="padding:5px"><span class="pretsqu3"></span></td>
                                                  <td>&ge; {{ ega_mean_avg_values[2] }} &amp; &lt; {{ ega_mean_avg_values[3] }}</td>
                                                </tr>
                                                <tr>
                                                  <td style="padding:5px"><span class="pretsqu4"></span></td>
                                                    <td>&ge; {{ ega_mean_avg_values[3] }}</td>
                                                </tr>
                                                <tr>
                                                  <td style="padding:5px"><span class="squfill"></span></td>
                                                  <td>No Data {{ ega_mean_avg_values[0] }}</td>
                                                </tr>
                                              </q-markup-table>
                                            </font>
                                          </q-popup-proxy>
                                        </q-btn>
                                      </td>
                                    </tr>
                                  </table>
                                  <!-- // legend -->
                                </tr>
                                <tr>
                                  <td>
                                    <q-toggle
                                      :label="`mean of gestational age calculated from last menstrual period (LMP) full cohort ${ fc_calcega_mean_avgModel2 }`"
                                      v-on:input="showMap2PanelToggleLayer('fc_calcega_mean_avg')"
                                      color="teal"
                                      false-value="Not Selected"
                                      true-value="Selected"
                                      v-model="fc_calcega_mean_avgModel2"
                                    >
                                      <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">Arithmetic mean of gestational age calculated from last menstrual period (LMP) for full cohort</q-tooltip>
                                    </q-toggle>
                                  </td>
                                </tr>
                                <tr>
                                  <td>
                                    <q-toggle
                                      :label="`mean of gestational age based on clinical estimate full cohorts ${ fc_clinega_mean_avgModel2 }`"
                                      v-on:input="showMap2PanelToggleLayer('fc_clinega_mean_avg')"
                                      color="teal"
                                      false-value="Not Selected"
                                      true-value="Selected"
                                      v-model="fc_clinega_mean_avgModel2"
                                    >
                                      <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">Arithmetic mean of gestational age based on clinical estimate for full cohort</q-tooltip>
                                    </q-toggle>
                                  </td>
                                </tr>
                                <tr>
                                  <td>
                                    <q-toggle
                                      :label="`mean of gestational age calculated from last menstrual period (LMP) singleton cohort ${ sc_calcega_mean_avgModel2 }`"
                                      v-on:input="showMap2PanelToggleLayer('sc_calcega_mean_avg')"
                                      color="teal"
                                      false-value="Not Selected"
                                      true-value="Selected"
                                      v-model="sc_calcega_mean_avgModel2"
                                    >
                                      <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">arithmetic mean of gestational age calculated from last menstrual period (LMP) for singleton cohort</q-tooltip>
                                    </q-toggle>
                                  </td>
                                </tr>
                                <tr>
                                  <td>
                                    <q-toggle
                                      :label="`mean of gestational age based on clinical estimate singleton cohorts ${ sc_clinega_mean_avgModel2 }`"
                                      v-on:input="showMap2PanelToggleLayer('sc_clinega_mean_avg')"
                                      color="teal"
                                      false-value="Not Selected"
                                      true-value="Selected"
                                      v-model="sc_clinega_mean_avgModel2"
                                    >
                                      <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">Arithmetic mean of gestational age based on clinical estimate for singleton cohort</q-tooltip>
                                    </q-toggle>
                                  </td>
                                </tr>
                                <tr>
                                  <table cellspacing="3" cellpadding="0" style="width:100%">
                                    <tr>
                                      <!-- // legend -->
                                      <td>
                                        Preterm births Legend
                                      </td>
                                      <td>
                                        <q-tooltip>Click to View Map Legend</q-tooltip>
                                        <q-btn flat dense round icon="fas fa-list" class="teal text-black" aria-label="Map Legend">
                                          <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
                                            <font size="2" face="Arial" >
                                              <q-markup-table dense class="bg-teal-1">
                                                <tr>
                                                   <td style="text-align:center;" colspan="2">Percent preterm births</td>
                                                </tr>
                                                <tr>
                                                  <td style="padding:5px"><span class="pretsqu1"></span></td>
                                                  <td>&lt; {{ preterm_percentage_values[1] }}</td>
                                                </tr>
                                                <tr>
                                                  <td style="padding:5px"><span class="pretsqu2"></span></td>
                                                  <td>&ge; {{ preterm_percentage_values[1] }} &amp; &lt; {{ preterm_percentage_values[2] }}</td>
                                                </tr>
                                                <tr>
                                                  <td style="padding:5px"><span class="pretsqu3"></span></td>
                                                  <td>&ge; {{ preterm_percentage_values[2] }} &amp; &lt; {{ preterm_percentage_values[3] }}</td>
                                                </tr>
                                                <tr>
                                                  <td style="padding:5px"><span class="pretsqu4"></span></td>
                                                    <td>&ge; {{ preterm_percentage_values[3] }}</td>
                                                </tr>
                                                <tr>
                                                  <td style="padding:5px"><span class="squfill"></span></td>
                                                  <td>No Data {{ preterm_percentage_values[0] }}</td>
                                                </tr>
                                              </q-markup-table>
                                            </font>
                                          </q-popup-proxy>
                                        </q-btn>
                                      </td>
                                      <!-- // legend -->
                                    </tr>
                                  </table>
                                </tr>
                                <tr>
                                  <td>
                                    <q-toggle
                                      :label="`percent preterm births, calculated from last menstrual period (LMP) for full cohort ${ fc_calcpreterm_percentageModel2 }`"
                                      v-on:input="showMap2PanelToggleLayer('fc_calcpreterm_percentage')"
                                      color="teal"
                                      false-value="Not Selected"
                                      true-value="Selected"
                                      v-model="fc_calcpreterm_percentageModel2"
                                    >
                                      <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">percentage of all observations with complete data that are preterm births, where preterm birth status is derived from gestational age calculated from last menstrual period (LMP) for full cohort</q-tooltip>
                                    </q-toggle>
                                  </td>
                                </tr>
                                <tr>
                                  <td>
                                    <q-toggle
                                      :label="`percent preterm births, based on clinical estimate full cohorts ${ fc_clinpreterm_percentageModel2 }`"
                                      v-on:input="showMap2PanelToggleLayer('fc_clinpreterm_percentage')"
                                      color="teal"
                                      false-value="Not Selected"
                                      true-value="Selected"
                                      v-model="fc_clinpreterm_percentageModel2"
                                    >
                                      <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">percentage of all observations with complete data that are preterm births, where preterm birth status is based on clinical estimate for full cohort</q-tooltip>
                                    </q-toggle>
                                  </td>
                                </tr>
                                <tr>
                                  <td>
                                    <q-toggle
                                      :label="`percent preterm births, calculated from last menstrual period (LMP) singleton cohort ${ sc_calcpreterm_percentageModel2 }`"
                                      v-on:input="showMap2PanelToggleLayer('sc_calcpreterm_percentage')"
                                      color="teal"
                                      false-value="Not Selected"
                                      true-value="Selected"
                                      v-model="sc_calcpreterm_percentageModel2"
                                    >
                                      <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">percentage of all observations with complete data that are preterm births, where preterm birth status is derived from gestational age calculated from last menstrual period (LMP) for singleton cohort</q-tooltip>
                                    </q-toggle>
                                  </td>
                                </tr>
                                <tr>
                                  <td>
                                    <q-toggle
                                      :label="`percent preterm births, based on clinical estimate singleton cohorts ${ sc_clinpreterm_percentageModel2 }`"
                                      v-on:input="showMap2PanelToggleLayer('sc_clinpreterm_percentage')"
                                      color="teal"
                                      false-value="Not Selected"
                                      true-value="Selected"
                                      v-model="sc_clinpreterm_percentageModel2"
                                    >
                                      <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">percentage of all observations with complete data that are preterm births, where preterm birth status is based on clinical estimate singleton cohort</q-tooltip>
                                    </q-toggle>
                                  </td>
                                </tr>
                              </table>
                            </div>
                          </q-list>
                        </q-menu>
                      </q-item>
                    </q-list>
                  </q-menu>
                </q-item>
                <!-- // Health layers -->

                <q-item clickable>
                  <q-item-section>Additional Features</q-item-section>
                  <q-item-section side>
                    <q-icon name="keyboard_arrow_right"></q-icon>
                  </q-item-section>

                  <q-menu anchor="top end" self="top start" content-class="bg-teal-1">
                    <q-list>
                      <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From North Carolina One Map</q-tooltip>
                      <div class="q-pa-md q-gutter-y-sm column">
                        <q-toggle
                          :label="`North Carolina County Boundaries ${ ncCountiesModel2 }`"
                          v-on:input="showMap2PanelToggleLayer('nccounties')"
                          color="teal"
                          false-value="Not Selected"
                          true-value="Selected"
                          v-model="ncCountiesModel2"
                        />
                      </div>
                    </q-list>
                  </q-menu>
                </q-item>
                <q-separator></q-separator>
                <q-item clickable v-close-popup>
                  <q-item-section>Close</q-item-section>
                </q-item>
              </q-list>
            </q-menu>
          </q-btn>
          <q-toolbar-title class="text-black">NC-Enviroscan Dual Map Two</q-toolbar-title>
          <q-tabs v-model="mapsynctab" v-on:input="MapSyncing()" no-caps class="bg-teal text-black">
            <q-tab name="syncmaps" label="Sync Maps" />
            <q-tab name="unsyncmaps" label="Unsync Maps" />
          </q-tabs>
        </q-toolbar>
        <!-- // Map Two Toolbar and Menu -->
        </div>
      </q-header>

      <div class="wrapper">
        <!--// app map1 -->
        <vl-map v-if="mapVisible" class="dualmap" ref="map1" :load-tiles-while-animating="true" :load-tiles-while-interacting="true"
          @singleclick="onMap1Click" data-projection="EPSG:4326" :default-controls="defaultControls" @mounted="onMapMounted"
          :controls="false" style="height:1200px">
          <!--//map1 view aka ol.View -->
          <div v-if="mapSync === 'False'">
            <vl-view ref="view1" :center.sync="center1" :zoom.sync="zoom1" :rotation.sync="rotation"></vl-view>
          </div>
          <div v-else>
            <vl-view ref="view1" :center.sync="center" :zoom.sync="zoom" :rotation.sync="rotation"></vl-view>
          </div>

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
          <vl-layer-tile v-for="layer in baseLayers1" :key="layer.name" :id="layer.name" :visible="layer.visible">
            <component ref="baselayer1" :is="'vl-source-' + layer.name" v-bind="layer"></component>
          </vl-layer-tile>
          <!--// base layers1 -->

          <!--// other layers1 from config -->
          <!-- eslint-disable vue/no-use-v-if-with-v-for,vue/no-confusing-v-for-v-if -->
          <vl-layer-vector-tile v-for="layer in layers1" :is="layer.cmp" v-if="layer.visible" :key="layer.id" v-bind="layer">
            <!--// add vl-source-* -->
            <component ref="layer1Source" :is="layer.source.cmp" v-bind="layer.source" />
            <!--// add style components if provided -->
            <!--// create vl-style-box or vl-style-func -->
            <component ref="layer1Style" v-if="layer.style" v-for="(style, i) in layer.style" :key="i" :is="style.cmp" v-bind="style" />
          </vl-layer-vector-tile>
          <!-- eslint-enable vue/no-use-v-if-with-v-for,vue/no-confusing-v-for-v-if -->
          <!--// other layers1 -->
        </vl-map>
        <!--// app map1 -->

        <!--// app map2 -->
        <vl-map v-if="mapVisible" class="dualmap" ref="map2" :load-tiles-while-animating="true" :load-tiles-while-interacting="true"
          @singleclick="onMap2Click" data-projection="EPSG:4326"  :default-controls="defaultControls" @mounted="onMapMounted"
          :controls="false" style="height:1200px">
           <!--// map2 view aka ol.View -->
          <div v-if="mapSync === 'False'">
            <vl-view ref="view2" :center.sync="center2" :zoom.sync="zoom2" :rotation.sync="rotation"></vl-view>
          </div>
          <div v-else>
            <vl-view ref="view2" :center.sync="center" :zoom.sync="zoom" :rotation.sync="rotation"></vl-view>
          </div>

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

          <!--// base layers2 -->
          <vl-layer-tile v-for="layer in baseLayers2" :key="layer.name" :id="layer.name" :visible="layer.visible">
            <component  ref="baselayer2" :is="'vl-source-' + layer.name" v-bind="layer"></component>
          </vl-layer-tile>
          <!--// base layers2 -->

          <!--// other layers2 from config -->
          <!-- eslint-disable vue/no-use-v-if-with-v-for,vue/no-confusing-v-for-v-if -->
          <vl-layer-vector-tile v-for="layer in layers2" :is="layer.cmp" v-if="layer.visible" :key="layer.id" v-bind="layer">
            <!--// add vl-source-* -->
            <component ref="layer2Source" :is="layer.source.cmp" v-bind="layer.source" />
            <!--// add style components if provided -->
            <!--// create vl-style-box or vl-style-func -->
            <component ref="layer2Style" v-if="layer.style" v-for="(style, i) in layer.style" :key="i" :is="style.cmp" v-bind="style" />
          </vl-layer-vector-tile>
          <!-- eslint-enable vue/no-use-v-if-with-v-for,vue/no-confusing-v-for-v-if -->
          <!--// other layers2 -->
        </vl-map>
        <!--// app map2 -->
      </div>

      <!--// Go to Single Screen Map button -->
      <q-page-sticky position="top-left" :offset="[78, 28]">
        <q-btn flat round dense icon="far fa-square" class="bg-teal text-black" aria-label="Single Screen Map" @click="$router.replace('/')">
          <q-tooltip>Go to Single Screen Map</q-tooltip>
        </q-btn>
      </q-page-sticky>
      <!--// Go to Single Screen Map button -->

      <!--// ol map1 controls -->
      <q-page-sticky position="top-left" :offset="[18, 18]">
        <div id="Zoom1Target"></div>
      </q-page-sticky>
      <!-- q-page-sticky position="bottom-left" :offset="[8, 38]">
        <div id="OverviewMap1Target"></div>
      </q-page-sticky -->
      <q-page-sticky position="bottom-left" :offset="[15, 8]">
        <div id="Scale1Target"></div>
      </q-page-sticky>
      <!--// ol map1 controls -->

      <!--// NC Enviroscan Icon -->
      <q-page-sticky position="top-right" :offset="[98, 5]">
        <img src="statics/nc-enviroscan-110.png">
      </q-page-sticky>
      <!--// NC Enviroscan Icon -->

      <!--// ol map2 controls -->
      <q-page-sticky position="top-right" :offset="[58, 18]">
        <div id="Zoom2Target"></div>
      </q-page-sticky>
      <!--// ol map2 controls -->

      <!--// Fullscreen button -->
      <q-page-sticky position="top-right" :offset="[18, 98]">
        <q-btn color="teal" class="text-black" @click="$q.fullscreen.toggle()" round :icon="$q.fullscreen.isActive ? 'fullscreen_exit' : 'fullscreen'">
          <q-tooltip>Open &amp; Close Full Screen</q-tooltip>
        </q-btn>
      </q-page-sticky>
      <!--// Fullscreen button -->

      <!--// select location tools -->
      <q-page-sticky position="bottom-right" :offset="[18, 18]">
        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">Map Location Tools</q-tooltip>
        <q-fab icon="keyboard_arrow_up" direction="up" external-label color="teal text-black" label="Map Location Tools">
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

      <q-footer elevated class="bg-teal">
        <q-toolbar>
          <!-- q-toolbar-title class="q-mr-sm text-black">Footer</q-toolbar-title -->
          <!-- // Map1 interleave legend -->
          <div class="q-pa-md q-gutter-y-sm column text-black">
            Map One Interleave Legend
            <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
              <font size="2" face="Arial" >
                <q-markup-table dense class="bg-brown-1">
                  <tr>
                    <td style="text-align:center;" colspan="4"><span v-html="map1pat1title"></span></td>
                    <td style="text-align:center;"><span v-html="map1pat2title"></span></td>
                  </tr>
                  <tr>
                     <td>&lt; <span v-html="map1pat1val1"></span></td>
                     <td>&ge; <span v-html="map1pat1val1"></span> &amp; &lt; <span v-html="map1pat1val2"></span></td>
                     <td>&ge; <span v-html="map1pat1val2"></span> &amp; &lt; <span v-html="map1pat1val3"></span></td>
                     <td>&ge; <span v-html="map1pat1val3"></span></td>
                  </tr>
                  <tr>
                    <td style="padding:5px"><div class="vstr41"></div></td>
                    <td style="padding:5px"><div class="vstr42"></div></td>
                    <td style="padding:5px"><div class="vstr43"></div></td>
                    <td style="padding:5px"><div class="vstr44"></div></td>
                    <td>&ge; <span v-html="map1pat2val3"></span></td>
                  </tr>
                  <tr>
                    <td style="padding:5px"><div class="vstr31"></div></td>
                    <td style="padding:5px"><div class="vstr32"></div></td>
                    <td style="padding:5px"><div class="vstr33"></div></td>
                    <td style="padding:5px"><div class="vstr34"></div></td>
                    <td>&ge; <span v-html="map1pat2val2"></span> &amp; &lt; <span v-html="map1pat2val3"></span></td>
                  </tr>
                  <tr>
                    <td style="padding:5px"><div class="vstr21"></div></td>
                    <td style="padding:5px"><div class="vstr22"></div></td>
                    <td style="padding:5px"><div class="vstr23"></div></td>
                    <td style="padding:5px"><div class="vstr24"></div></td>
                    <td>&ge; <span v-html="map1pat2val1"></span> &amp; &lt; <span v-html="map1pat2val2"></span></td>
                  </tr>
                  <tr>
                    <td style="padding:5px"><div class="vstr11"></div></td>
                    <td style="padding:5px"><div class="vstr12"></div></td>
                    <td style="padding:5px"><div class="vstr13"></div></td>
                    <td style="padding:5px"><div class="vstr14"></div></td>
                    <td>&lt; <span v-html="map1pat2val1"></span></td>
                  </tr>
                  <tr>
                    <td style="padding:5px"><span class="vstrfill"></span></td>
                    <td>No Data -999.99</td>
                  </tr>
                </q-markup-table>
                <q-markup-table dense class="bg-brown-1">
                  <tr>
                    <td><span v-html="map1var1"></span></td>
                    <td><span v-html="map1var2"></span></td>
                  </tr>
                </q-markup-table>
              </font>
            </q-popup-proxy>
          </div>
          <!-- // Map1 interleave legend -->
          <q-space />
          <!-- // Map2 interleave legend -->
          <div class="q-pa-md q-gutter-y-sm column text-black">
            Map Two Interleave Legend
            <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
              <font size="2" face="Arial" >
                <q-markup-table dense class="bg-brown-1">
                  <tr>
                    <td style="text-align:center;" colspan="4"><span v-html="map2pat1title"></span></td>
                    <td style="text-align:center;"><span v-html="map2pat2title"></span></td>
                  </tr>
                  <tr>
                     <td>&lt; <span v-html="map2pat1val1"></span></td>
                     <td>&ge; <span v-html="map2pat1val1"></span> &amp; &lt; <span v-html="map2pat1val2"></span></td>
                     <td>&ge; <span v-html="map2pat1val2"></span> &amp; &lt; <span v-html="map2pat1val3"></span></td>
                     <td>&ge; <span v-html="map2pat1val3"></span></td>
                  </tr>
                  <tr>
                    <td style="padding:5px"><div class="vstr41"></div></td>
                    <td style="padding:5px"><div class="vstr42"></div></td>
                    <td style="padding:5px"><div class="vstr43"></div></td>
                    <td style="padding:5px"><div class="vstr44"></div></td>
                    <td>&ge; <span v-html="map2pat2val3"></span></td>
                  </tr>
                  <tr>
                    <td style="padding:5px"><div class="vstr31"></div></td>
                    <td style="padding:5px"><div class="vstr32"></div></td>
                    <td style="padding:5px"><div class="vstr33"></div></td>
                    <td style="padding:5px"><div class="vstr34"></div></td>
                    <td>&ge; <span v-html="map2pat2val2"></span> &amp; &lt; <span v-html="map2pat2val3"></span></td>
                  </tr>
                  <tr>
                    <td style="padding:5px"><div class="vstr21"></div></td>
                    <td style="padding:5px"><div class="vstr22"></div></td>
                    <td style="padding:5px"><div class="vstr23"></div></td>
                    <td style="padding:5px"><div class="vstr24"></div></td>
                    <td>&ge; <span v-html="map2pat2val1"></span> &amp; &lt; <span v-html="map2pat2val2"></span></td>
                  </tr>
                  <tr>
                    <td style="padding:5px"><div class="vstr11"></div></td>
                    <td style="padding:5px"><div class="vstr12"></div></td>
                    <td style="padding:5px"><div class="vstr13"></div></td>
                    <td style="padding:5px"><div class="vstr14"></div></td>
                    <td>&lt; <span v-html="map2pat2val1"></span></td>
                  </tr>
                  <tr>
                    <td style="padding:5px"><span class="vstrfill"></span></td>
                    <td>No Data -999.99</td>
                  </tr>
                </q-markup-table>
                <q-markup-table dense class="bg-brown-1">
                  <tr>
                    <td><span v-html="map2var1"></span></td>
                    <td><span v-html="map2var2"></span></td>
                  </tr>
                </q-markup-table>
              </font>
            </q-popup-proxy>
          </div>
          <!-- // Map2 pattern legend -->
        </q-toolbar>
      </q-footer>

    </q-page-container>
  </q-layout>
</template>

<script>
// quasar and vuelayers import
import { openURL } from 'quasar'
import { findPointOnSurface, createStyle } from 'vuelayers/lib/ol-ext'
// import { createStyle } from 'vuelayers/lib/ol-ext'
import { camelCase } from 'lodash'

// ol controls import
import ScaleLine from 'ol/control/ScaleLine'
// import OverviewMap from 'ol/control/OverviewMap'
import Zoom from 'ol/control/Zoom'
import Attribution from 'ol/control/Attribution'

// other ol imports
import { Style, Stroke, Fill } from 'ol/style'
import { DEVICE_PIXEL_RATIO } from 'ol/has.js'

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
  name: 'NC-Enviroscan-Dual',
  components: {
  },
  data () {
    return {
      // map parameters
      defaultControls: {
        attribution: true,
        rotate: false,
        zoom: false
      },
      mapsynctab: 'syncmaps',
      mapSync: 'True',
      center: [-79.0193, 35.0],
      center1: [-79.0193, 35.0],
      center2: [-79.0193, 35.0],
      getlocation: 'False',
      currentlocation: 'False',
      addresslocation: 'False',
      addressloc: [NaN, NaN],
      zoom: 8,
      zoom1: 8,
      zoom2: 8,
      rotation: 0,
      mapVisible: true,
      // Other layers attributes
      address: null,
      acceptaddress: false,
      vtSelection: {},
      vtIdProp: 'geoid10',
      cntlayer1: undefined,
      ncCountiesModel1: 'Not Selected',
      acslayer1: undefined,
      povertyModel1: 'Not Selected',
      nativeModel1: 'Not Selected',
      asianModel1: 'Not Selected',
      blackModel1: 'Not Selected',
      polyModel1: 'Not Selected',
      whiteModel1: 'Not Selected',
      tworacesModel1: 'Not Selected',
      hispModel1: 'Not Selected',
      nothispModel1: 'Not Selected',
      langModel1: 'Not Selected',
      ejslayer1: undefined,
      d_ldpnt_2Model1: 'Not Selected',
      d_dslpm_2Model1: 'Not Selected',
      d_cancr_2Model1: 'Not Selected',
      d_resp_2Model1: 'Not Selected',
      d_ptraf_2Model1: 'Not Selected',
      d_pwdis_2Model1: 'Not Selected',
      d_pnpl_2Model1: 'Not Selected',
      d_prmp_2Model1: 'Not Selected',
      d_ptsdf_2Model1: 'Not Selected',
      d_ozone_2Model1: 'Not Selected',
      d_pm25_2Model1: 'Not Selected',
      pretermlayer1: undefined,
      fc_calcega_mean_avgModel1: 'Not Selected',
      fc_clinega_mean_avgModel1: 'Not Selected',
      sc_calcega_mean_avgModel1: 'Not Selected',
      sc_clinega_mean_avgModel1: 'Not Selected',
      fc_calcpreterm_percentageModel1: 'Not Selected',
      fc_clinpreterm_percentageModel1: 'Not Selected',
      sc_calcpreterm_percentageModel1: 'Not Selected',
      sc_clinpreterm_percentageModel1: 'Not Selected',
      casespertenModel1: 'Not Selected',
      casesperhundredModel1: 'Not Selected',
      deathsModel1: 'Not Selected',
      cntlayer2: undefined,
      ncCountiesModel2: 'Not Selected',
      acslayer2: undefined,
      povertyModel2: 'Not Selected',
      nativeModel2: 'Not Selected',
      asianModel2: 'Not Selected',
      blackModel2: 'Not Selected',
      polyModel2: 'Not Selected',
      whiteModel2: 'Not Selected',
      tworacesModel2: 'Not Selected',
      hispModel2: 'Not Selected',
      nothispModel2: 'Not Selected',
      langModel2: 'Not Selected',
      ejslayer2: undefined,
      d_ldpnt_2Model2: 'Not Selected',
      d_dslpm_2Model2: 'Not Selected',
      d_cancr_2Model2: 'Not Selected',
      d_resp_2Model2: 'Not Selected',
      d_ptraf_2Model2: 'Not Selected',
      d_pwdis_2Model2: 'Not Selected',
      d_pnpl_2Model2: 'Not Selected',
      d_prmp_2Model2: 'Not Selected',
      d_ptsdf_2Model2: 'Not Selected',
      d_ozone_2Model2: 'Not Selected',
      d_pm25_2Model2: 'Not Selected',
      casespertenModel2: 'Not Selected',
      casesperhundredModel2: 'Not Selected',
      deathsModel2: 'Not Selected',
      pretermlayer2: undefined,
      fc_calcega_mean_avgModel2: 'Not Selected',
      fc_clinega_mean_avgModel2: 'Not Selected',
      sc_calcega_mean_avgModel2: 'Not Selected',
      sc_clinega_mean_avgModel2: 'Not Selected',
      fc_calcpreterm_percentageModel2: 'Not Selected',
      fc_clinpreterm_percentageModel2: 'Not Selected',
      sc_calcpreterm_percentageModel2: 'Not Selected',
      sc_clinpreterm_percentageModel2: 'Not Selected',
      // variable colors
      ncwellmap1style: 'nopattern',
      ncwellmap2style: 'nopattern',
      acsmap1style: 'nopattern',
      acsmap2style: 'nopattern',
      ejsmap1style: 'nopattern',
      ejsmap2style: 'nopattern',
      pretermmap1style: 'nopattern',
      pretermmap2style: 'nopattern',
      varcolor: null,
      pattern1colors: ['rgba(246, 250, 5, 1.0)', 'rgba(0, 125, 125, 1.0)', 'rgba(91, 240, 245, 1.0)', 'rgba(250, 203, 92, 1.0)', 'rgba(240, 129, 5, 1.0)'],
      // patternt1colors: ['246, 250, 5, 1.0', '0, 125, 125, 1.0', '91, 240, 245, 1.0', '250, 203, 92, 1.0', '240, 129, 5, 1.0'],
      pattern2colors: ['rgba(246, 250, 5, 1.0)', 'rgba(2, 114, 250, 1.0)', 'rgba(150, 215, 250, 1.0)', 'rgba(250, 219, 202, 1.0)', 'rgba(153, 55, 2, 1.0)'],
      // patternt2colors: ['246, 250, 5, 1.0', '2, 114, 250, 1.0', '150, 215, 250, 1.0', '250, 219, 202, 1.0', '153, 55, 2, 1.0'],
      arsncolors: ['rgba(91, 95, 99, 0.65)', 'rgba(247, 121, 237, 0.65)', 'rgba(194, 76, 237, 0.65)', 'rgba(165, 52, 235, 0.65)', 'rgba(127, 3, 252, 0.65)'],
      cadmcolors: ['rgba(91, 95, 99, 0.65)', 'rgba(223, 235, 52, 0.65)', 'rgba(235, 192, 52, 0.65)', 'rgba(235, 162, 52, 0.65)', 'rgba(235, 89, 52, 0.65)'],
      leadcolors: ['rgba(50, 110, 219, 0.65)', 'rgba(196, 200, 207, 0.65)', 'rgba(155, 158, 163, 0.65)', 'rgba(108, 112, 120, 0.65)', 'rgba(39, 40, 43, 0.65)'],
      mngncolors: ['rgba(91, 95, 99, 0.65)', 'rgba(194, 232, 190, 0.65)', 'rgba(81, 222, 67, 0.65)', 'rgba(25, 128, 11, 0.65)', 'rgba(14, 82, 5, 0.65)'],
      acscolors: ['rgba(91, 95, 99, 0.85)', 'rgba(252, 210, 211, 0.85)', 'rgba(247, 84, 90, 0.85)', 'rgba(212, 4, 9, 0.85)', 'rgba(122, 1, 5, 0.85)'],
      ejscolors: ['rgba(91, 95, 99, 0.65)', 'rgba(235, 252, 3, 0.65)', 'rgba(252, 186, 3, 0.65)', 'rgba(252, 128, 3, 0.65)', 'rgba(252, 82, 3, 0.65)'],
      covidcolors: ['rgba(91, 95, 99, 0.65)', 'rgba(34, 240, 219, 0.65)', 'rgba(34, 223, 240, 0.65)', 'rgba(34, 185, 240, 0.65)', 'rgba(22, 141, 245, 0.65)', 'rgba(22, 74, 245, 0.65)', 'rgba(23, 2, 247, 0.65)'],
      pretermcolors: ['rgba(91, 95, 99, 0.65)', 'rgba(207, 252, 242, 0.65)', 'rgba(140, 250, 224, 0.65)', 'rgba(46, 240, 162, 0.65)', 'rgba(3, 148, 90, 0.65)'],
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
      ega_mean_avg_values: [-999.99, 38.469, 38.633, 38.779],
      // fc_calcega_mean_avg_values: [-999.99, 38.469, 38.633, 38.779],
      // fc_clinega_mean_avg_values: [-999.99, 38.35, 38.497, 38.626],
      // sc_calcega_mean_avg_values: [-999.99, 38.593, 38.753, 38.911],
      // sc_clinega_mean_avg_values: [-999.99, 38.481, 38.627, 38.761],
      preterm_percentage_values: [-999.99, 9.554, 11.285, 13.197],
      // fc_calcpreterm_percentage_values: [-999.99, 11.242, 12.871, 14.779],
      // fc_clinpreterm_percentage_values: [-999.99, 9.253, 10.41, 11.936],
      // sc_calcpreterm_percentage_values: [-999.99, 9.554, 11.285, 13.197],
      // sc_clinpreterm_percentage_values: [-999.99, 7.429, 8.621, 10.0],
      map1pat1val1: 0,
      map1pat1val2: 0,
      map1pat1val3: 0,
      map1pat1title: 'None',
      map1pat2val1: 0,
      map1pat2val2: 0,
      map1pat2val3: 0,
      map1pat2title: 'None',
      map1var1: 'None',
      map1var2: 'None',
      map2pat1val1: 0,
      map2pat1val2: 0,
      map2pat1val3: 0,
      map2pat1title: 'None',
      map2pat2val1: 0,
      map2pat2val2: 0,
      map2pat2val3: 0,
      map2pat2title: 'None',
      map2var1: 'None',
      map2var2: 'None',
      // baselayers config
      baselayer1: 'osm',
      baselayer2: 'osm',
      baseLayers1: [
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
      baseLayers2: [
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
      currentradiovariable1: 'ncwellwise_arsenic_med',
      currentacsvariable1: 'percent_below_poverty_level',
      currentpretermvariable1: 'fc_calcega_mean_avg',
      currentejsvariable1: 'd_ldpnt_2',
      currentradiovariable2: 'ncwellwise_arsenic_med',
      currentacsvariable2: 'percent_below_poverty_level',
      currentpretermvariable2: 'fc_calcega_mean_avg',
      layers1: [
        {
          id: this.getNCWellwiseLayer1ID(),
          title: 'NC Wellwise Layer 1',
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
              factory: this.getncwellwiseStyle1
            }
          ]
        },
        {
          id: this.getACSCensusLayer1ID(),
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
              factory: this.getacsStyle1
            }
          ]
        },
        {
          id: this.getEJScreenLayer1ID(),
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
              factory: this.getejscreenStyle1
            }
          ]
        },
        {
          id: this.getCovid19Layer1ID(),
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
              factory: this.getcovid19Style1
            }
          ]
        },
        {
          id: this.getPreTermLayer1ID(),
          title: 'PreTerm',
          cmp: 'vl-layer-vector-tile',
          visible: false,
          source: {
            cmp: 'vl-source-vector-tile',
            url: 'http://' + pubhost[0].PUBHOST_URL + '/drf/apimvt/v1/data/nc_preterm_subset_geom.mvt?tile={z}/{x}/{y}'
          },
          style: [
            {
              cmp: 'vl-style-func',
              factory: this.getpretermStyle1
            }
          ]
        },
        {
          id: 'ncCounties1',
          title: 'NC Counties1',
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
          id: 'noLayer1',
          title: 'No Layer1',
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
      ],
      layers2: [
        {
          id: this.getNCWellwiseLayer2ID(),
          title: 'NC Wellwise Layer 2',
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
              factory: this.getncwellwiseStyle2
            }
          ]
        },
        {
          id: this.getACSCensusLayer2ID(),
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
              factory: this.getacsStyle2
            }
          ]
        },
        {
          id: this.getEJScreenLayer2ID(),
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
              factory: this.getejscreenStyle2
            }
          ]
        },
        {
          id: this.getCovid19Layer2ID(),
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
              factory: this.getcovid19Style2
            }
          ]
        },
        {
          id: this.getPreTermLayer2ID(),
          title: 'PreTerm',
          cmp: 'vl-layer-vector-tile',
          visible: false,
          source: {
            cmp: 'vl-source-vector-tile',
            url: 'http://' + pubhost[0].PUBHOST_URL + '/drf/apimvt/v1/data/nc_preterm_subset_geom.mvt?tile={z}/{x}/{y}'
          },
          style: [
            {
              cmp: 'vl-style-func',
              factory: this.getpretermStyle2
            }
          ]
        },
        {
          id: 'ncCounties2',
          title: 'NC Counties2',
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
          id: 'noLayer2',
          title: 'No Layer2',
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
        this.center1 = [coordinates.lng, coordinates.lat]
        this.center2 = [coordinates.lng, coordinates.lat]
      }) */
  },
  computed: {
    pattern1Colors () {
      return {
        '--pattern1-colors': this.pattern1colors
      }
    },
    pattern2Colors () {
      return {
        '--pattern2-colors': this.pattern2colors
      }
    },
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
    },
    pretermColors () {
      return {
        '--preterm-colors': this.pretermcolors
      }
    }
  },
  methods: {
    openURL,
    camelCase,
    pointOnSurface: findPointOnSurface,
    MapSyncing () {
      if (this.mapsynctab === 'syncmaps') {
        this.mapSync = 'True'
      } else if (this.mapsynctab === 'unsyncmaps') {
        this.mapSync = 'False'
      }
    },
    getZoom1 () {
      let zoom
      if (this.mapSync === 'True') {
        zoom = this.zoom
        this.zoom1 = this.zoom
      } else if (this.mapSync === 'False') {
        zoom = this.zoom1
      }
      return zoom
    },
    getZoom2 () {
      let zoom
      if (this.mapSync === 'True') {
        zoom = this.zoom
        this.zoom1 = this.zoom
      } else if (this.mapSync === 'False') {
        zoom = this.zoom2
      }
      return zoom
    },
    getCurrentLocation () {
      if (this.getlocation === 'True') {
        this.addresslocation = 'False'
        this.currentlocation = 'True'
        this.zoom = 10
        this.zoom1 = 10
        this.zoom2 = 10
      } else if (this.getlocation === 'False') {
        this.currentlocation = 'False'
        this.zoom = 8
        this.zoom1 = 8
        this.zoom2 = 8
        this.center = [-79.0193, 35.0]
        this.center1 = [-79.0193, 35.0]
        this.center2 = [-79.0193, 35.0]
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
          this.center1 = [Number(response[0].lon), Number(response[0].lat)]
          this.center2 = [Number(response[0].lon), Number(response[0].lat)]
          this.addressloc = [Number(response[0].lon), Number(response[0].lat)]
          this.zoom = 10
          this.zoom1 = 10
          this.zoom2 = 10
        })
        .catch((error) => {
          console.log(error)
        })
    },
    resetAddress () {
      this.address = null
      this.acceptaddress = false
    },
    getPattern1: function (color2) {
      let canvas = document.createElement('canvas')
      let context = canvas.getContext('2d')
      let pixelRatio = DEVICE_PIXEL_RATIO
      canvas.width = 8 * pixelRatio
      canvas.height = 8 * pixelRatio
      let color1 = 'rgb(0, 0, 0, 0.0)'
      let numberOfStripes = 50
      for (var i = 0; i < numberOfStripes; i++) {
        var thickness = 200 / numberOfStripes
        context.beginPath()
        context.strokeStyle = i % 2 ? color1 : color2
        context.lineWidth = thickness
        context.lineCap = 'round'

        context.moveTo(i * thickness + thickness / 2, 0)
        context.lineTo(i * thickness + thickness / 2, 300)
        context.stroke()
      }
      return context.createPattern(canvas, 'repeat')
    },
    getPattern2: function (color1) {
      let canvas = document.createElement('canvas')
      let context = canvas.getContext('2d')
      let pixelRatio = DEVICE_PIXEL_RATIO
      canvas.width = 8 * pixelRatio
      canvas.height = 8 * pixelRatio
      let color2 = 'rgb(0, 0, 0, 0.0)'
      let numberOfStripes = 50
      for (var i = 0; i < numberOfStripes; i++) {
        var thickness = 200 / numberOfStripes
        context.beginPath()
        context.strokeStyle = i % 2 ? color1 : color2
        context.lineWidth = thickness
        context.lineCap = 'round'

        context.moveTo(i * thickness + thickness / 2, 0)
        context.lineTo(i * thickness + thickness / 2, 300)
        context.stroke()
      }
      return context.createPattern(canvas, 'repeat')
    },
    getColors: function (data, values, colors, variable, layer) {
      if (colors.length === 7) {
        if (data[variable] === values[0]) {
          this.varcolor = colors[0]
        } else if (data[variable] < values[1]) {
          this.varcolor = colors[1]
        } else if (data[variable] >= values[1] && data[variable] < values[2]) {
          this.varcolor = colors[2]
        } else if (data[variable] >= values[2] && data[variable] < values[3]) {
          this.varcolor = colors[3]
        } else if (data[variable] >= values[3] && data[variable] < values[4]) {
          this.varcolor = colors[4]
        } else if (data[variable] >= values[4] && data[variable] < values[5]) {
          this.varcolor = colors[5]
        } else if (data[variable] >= values[5]) {
          this.varcolor = colors[6]
        }
      } else if (colors.length === 6) {
        if (data[variable.substring(11)] === values[0]) {
          this.varcolor = colors[0]
        } else if (data[variable.substring(11)] < values[1]) {
          this.varcolor = colors[1]
        } else if (data[variable.substring(11)] >= values[1] && data[variable.substring(11)] < values[2]) {
          this.varcolor = colors[2]
        } else if (data[variable.substring(11)] >= values[2] && data[variable.substring(11)] < values[3]) {
          this.varcolor = colors[3]
        } else if (data[variable.substring(11)] >= values[3] && data[variable.substring(11)] < values[4]) {
          this.varcolor = colors[4]
        } else if (data[variable.substring(11)] >= values[4]) {
          this.varcolor = colors[5]
        }
      } else if (colors.length === 5) {
        if (layer.substring(0, layer.length - 1) === 'ncwelllayer') {
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
    getPatternColors: function (data, values, colors, variable, layer) {
      if (layer.substr(-1) === '1') {
        if (layer.substring(0, layer.length - 1) === 'ncwelllayer') {
          let getPattern
          let patternColors
          if (layer === 'ncwelllayer1') {
            if (this.ncwellmap1style === 'pattern1') {
              this.map1pat1val1 = values[1]
              this.map1pat1val2 = values[2]
              this.map1pat1val3 = values[3]
              this.map1pat1title = variable
              getPattern = this.getPattern1
              patternColors = this.pattern1colors
            } else if (this.ncwellmap1style === 'pattern2') {
              this.map1pat2val1 = values[1]
              this.map1pat2val2 = values[2]
              this.map1pat2val3 = values[3]
              this.map1pat2title = variable
              getPattern = this.getPattern2
              patternColors = this.pattern2colors
            }
          } else if (layer === 'ncwelllayer2') {
            if (this.ncwellmap2style === 'pattern1') {
              this.map1pat1val1 = values[1]
              this.map1pat1val2 = values[2]
              this.map1pat1val3 = values[3]
              this.map1pat1title = variable
              getPattern = this.getPattern1
              patternColors = this.pattern1colors
            } else if (this.ncwellmap2style === 'pattern2') {
              this.map1pat2val1 = values[1]
              this.map1pat2val2 = values[2]
              this.map1pat2val3 = values[3]
              this.map1pat2title = variable
              getPattern = this.getPattern2
              patternColors = this.pattern2colors
            }
          }
          if (data[variable.substring(11)] === values[0]) {
            this.varcolor = getPattern(patternColors[0])
          } else if (data[variable.substring(11)] < values[1]) {
            this.varcolor = getPattern(patternColors[1])
          } else if (data[variable.substring(11)] >= values[1] && data[variable.substring(11)] < values[2]) {
            this.varcolor = getPattern(patternColors[2])
          } else if (data[variable.substring(11)] >= values[2] && data[variable.substring(11)] < values[3]) {
            this.varcolor = getPattern(patternColors[3])
          } else if (data[variable.substring(11)] >= values[3]) {
            this.varcolor = getPattern(patternColors[4])
          }
        } else {
          let getPattern
          let patternColors
          if (layer === 'acslayer1') {
            if (this.acsmap1style === 'pattern1') {
              this.map1pat1val1 = values[1]
              this.map1pat1val2 = values[2]
              this.map1pat1val3 = values[3]
              this.map1pat1title = variable
              getPattern = this.getPattern1
              patternColors = this.pattern1colors
            } else if (this.acsmap1style === 'pattern2') {
              this.map1pat2val1 = values[1]
              this.map1pat2val2 = values[2]
              this.map1pat2val3 = values[3]
              this.map1pat2title = variable
              getPattern = this.getPattern2
              patternColors = this.pattern2colors
            }
          } else if (layer === 'acslayer2') {
            if (this.acsmap2style === 'pattern1') {
              this.map1pat1val1 = values[1]
              this.map1pat1val2 = values[2]
              this.map1pat1val3 = values[3]
              this.map1pat1title = variable
              getPattern = this.getPattern1
              patternColors = this.pattern1colors
            } else if (this.acsmap2style === 'pattern2') {
              this.map1pat2val1 = values[1]
              this.map1pat2val2 = values[2]
              this.map1pat2val3 = values[3]
              this.map1pat2title = variable
              getPattern = this.getPattern2
              patternColors = this.pattern2colors
            }
          } else if (layer === 'ejslayer1') {
            if (this.ejsmap1style === 'pattern1') {
              this.map1pat1val1 = values[1]
              this.map1pat1val2 = values[2]
              this.map1pat1val3 = values[3]
              this.map1pat1title = variable
              getPattern = this.getPattern1
              patternColors = this.pattern1colors
            } else if (this.ejsmap1style === 'pattern2') {
              this.map1pat2val1 = values[1]
              this.map1pat2val2 = values[2]
              this.map1pat2val3 = values[3]
              this.map1pat2title = variable
              getPattern = this.getPattern2
              patternColors = this.pattern2colors
            }
          } else if (layer === 'ejslayer2') {
            if (this.ejsmap2style === 'pattern1') {
              this.map1pat1val1 = values[1]
              this.map1pat1val2 = values[2]
              this.map1pat1val3 = values[3]
              this.map1pat1title = variable
              getPattern = this.getPattern1
              patternColors = this.pattern1colors
            } else if (this.ejsmap2style === 'pattern2') {
              this.map1pat2val1 = values[1]
              this.map1pat2val2 = values[2]
              this.map1pat2val3 = values[3]
              this.map1pat2title = variable
              getPattern = this.getPattern2
              patternColors = this.pattern2colors
            }
          } else if (layer === 'pretermlayer1') {
            if (this.pretermmap1style === 'pattern1') {
              this.map1pat1val1 = values[1]
              this.map1pat1val2 = values[2]
              this.map1pat1val3 = values[3]
              this.map1pat1title = variable
              getPattern = this.getPattern1
              patternColors = this.pattern1colors
            } else if (this.pretermmap1style === 'pattern2') {
              this.map1pat2val1 = values[1]
              this.map1pat2val2 = values[2]
              this.map1pat2val3 = values[3]
              this.map1pat2title = variable
              getPattern = this.getPattern2
              patternColors = this.pattern2colors
            }
          } else if (layer === 'pretermlayer2') {
            if (this.pretermmap2style === 'pattern1') {
              this.map1pat1val1 = values[1]
              this.map1pat1val2 = values[2]
              this.map1pat1val3 = values[3]
              this.map1pat1title = variable
              getPattern = this.getPattern1
              patternColors = this.pattern1colors
            } else if (this.pretermmap2style === 'pattern2') {
              this.map1pat2val1 = values[1]
              this.map1pat2val2 = values[2]
              this.map1pat2val3 = values[3]
              this.map1pat2title = variable
              getPattern = this.getPattern2
              patternColors = this.pattern2colors
            }
          }
          if (data[variable] === values[0]) {
            this.varcolor = getPattern(patternColors[0])
          } else if (data[variable] < values[1]) {
            this.varcolor = getPattern(patternColors[1])
          } else if (data[variable] >= values[1] && data[variable] < values[2]) {
            this.varcolor = getPattern(patternColors[2])
          } else if (data[variable] >= values[2] && data[variable] < values[3]) {
            this.varcolor = getPattern(patternColors[3])
          } else if (data[variable] >= values[3]) {
            this.varcolor = getPattern(patternColors[4])
          }
        }
      } else if (layer.substr(-1) === '2') {
        if (layer.substring(0, layer.length - 1) === 'ncwelllayer') {
          let getPattern
          let patternColors
          if (layer === 'ncwelllayer1') {
            if (this.ncwellmap1style === 'pattern1') {
              this.map2pat1val1 = values[1]
              this.map2pat1val2 = values[2]
              this.map2pat1val3 = values[3]
              this.map2pat1title = variable
              getPattern = this.getPattern1
              patternColors = this.pattern1colors
            } else if (this.ncwellmap1style === 'pattern2') {
              this.map2pat2val1 = values[1]
              this.map2pat2val2 = values[2]
              this.map2pat2val3 = values[3]
              this.map2pat2title = variable
              getPattern = this.getPattern2
              patternColors = this.pattern2colors
            }
          } else if (layer === 'ncwelllayer2') {
            if (this.ncwellmap2style === 'pattern1') {
              this.map2pat1val1 = values[1]
              this.map2pat1val2 = values[2]
              this.map2pat1val3 = values[3]
              this.map2pat1title = variable
              getPattern = this.getPattern1
              patternColors = this.pattern1colors
            } else if (this.ncwellmap2style === 'pattern2') {
              this.map2pat2val1 = values[1]
              this.map2pat2val2 = values[2]
              this.map2pat2val3 = values[3]
              this.map2pat2title = variable
              getPattern = this.getPattern2
              patternColors = this.pattern2colors
            }
          }
          if (data[variable.substring(11)] === values[0]) {
            this.varcolor = getPattern(patternColors[0])
          } else if (data[variable.substring(11)] < values[1]) {
            this.varcolor = getPattern(patternColors[1])
          } else if (data[variable.substring(11)] >= values[1] && data[variable.substring(11)] < values[2]) {
            this.varcolor = getPattern(patternColors[2])
          } else if (data[variable.substring(11)] >= values[2] && data[variable.substring(11)] < values[3]) {
            this.varcolor = getPattern(patternColors[3])
          } else if (data[variable.substring(11)] >= values[3]) {
            this.varcolor = getPattern(patternColors[4])
          }
        } else {
          let getPattern
          let patternColors
          if (layer === 'acslayer1') {
            if (this.acsmap1style === 'pattern1') {
              this.map2pat1val1 = values[1]
              this.map2pat1val2 = values[2]
              this.map2pat1val3 = values[3]
              this.map2pat1title = variable
              getPattern = this.getPattern1
              patternColors = this.pattern1colors
            } else if (this.acsmap1style === 'pattern2') {
              this.map2pat2val1 = values[1]
              this.map2pat2val2 = values[2]
              this.map2pat2val3 = values[3]
              this.map2pat2title = variable
              getPattern = this.getPattern2
              patternColors = this.pattern2colors
            }
          } else if (layer === 'acslayer2') {
            if (this.acsmap2style === 'pattern1') {
              this.map2pat1val1 = values[1]
              this.map2pat1val2 = values[2]
              this.map2pat1val3 = values[3]
              this.map2pat1title = variable
              getPattern = this.getPattern1
              patternColors = this.pattern1colors
            } else if (this.acsmap2style === 'pattern2') {
              this.map2pat2val1 = values[1]
              this.map2pat2val2 = values[2]
              this.map2pat2val3 = values[3]
              this.map2pat2title = variable
              getPattern = this.getPattern2
              patternColors = this.pattern2colors
            }
          } else if (layer === 'ejslayer1') {
            if (this.ejsmap1style === 'pattern1') {
              this.map2pat1val1 = values[1]
              this.map2pat1val2 = values[2]
              this.map2pat1val3 = values[3]
              this.map2pat1title = variable
              getPattern = this.getPattern1
              patternColors = this.pattern1colors
            } else if (this.ejsmap1style === 'pattern2') {
              this.map2pat2val1 = values[1]
              this.map2pat2val2 = values[2]
              this.map2pat2val3 = values[3]
              this.map2pat2title = variable
              getPattern = this.getPattern2
              patternColors = this.pattern2colors
            }
          } else if (layer === 'ejslayer2') {
            if (this.ejsmap2style === 'pattern1') {
              this.map2pat1val1 = values[1]
              this.map2pat1val2 = values[2]
              this.map2pat1val3 = values[3]
              this.map2pat1title = variable
              getPattern = this.getPattern1
              patternColors = this.pattern1colors
            } else if (this.ejsmap2style === 'pattern2') {
              this.map2pat2val1 = values[1]
              this.map2pat2val2 = values[2]
              this.map2pat2val3 = values[3]
              this.map2pat2title = variable
              getPattern = this.getPattern2
              patternColors = this.pattern2colors
            }
          } else if (layer === 'pretermlayer1') {
            if (this.pretermmap1style === 'pattern1') {
              this.map2pat1val1 = values[1]
              this.map2pat1val2 = values[2]
              this.map2pat1val3 = values[3]
              this.map2pat1title = variable
              getPattern = this.getPattern1
              patternColors = this.pattern1colors
            } else if (this.pretermmap1style === 'pattern2') {
              this.map2pat2val1 = values[1]
              this.map2pat2val2 = values[2]
              this.map2pat2val3 = values[3]
              this.map2pat2title = variable
              getPattern = this.getPattern2
              patternColors = this.pattern2colors
            }
          } else if (layer === 'pretermlayer2') {
            if (this.pretermmap2style === 'pattern1') {
              this.map2pat1val1 = values[1]
              this.map2pat1val2 = values[2]
              this.map2pat1val3 = values[3]
              this.map2pat1title = variable
              getPattern = this.getPattern1
              patternColors = this.pattern1colors
            } else if (this.pretermmap2style === 'pattern2') {
              this.map2pat2val1 = values[1]
              this.map2pat2val2 = values[2]
              this.map2pat2val3 = values[3]
              this.map2pat2title = variable
              getPattern = this.getPattern2
              patternColors = this.pattern2colors
            }
          }
          if (data[variable] === values[0]) {
            this.varcolor = getPattern(patternColors[0])
          } else if (data[variable] < values[1]) {
            this.varcolor = getPattern(patternColors[1])
          } else if (data[variable] >= values[1] && data[variable] < values[2]) {
            this.varcolor = getPattern(patternColors[2])
          } else if (data[variable] >= values[2] && data[variable] < values[3]) {
            this.varcolor = getPattern(patternColors[3])
          } else if (data[variable] >= values[3]) {
            this.varcolor = getPattern(patternColors[4])
          }
        }
      }
    },
    getncwellwiseStyle1: function () {
      let getStyle
      if (this.ncwellmap1style === 'nopattern') {
        getStyle = this.getColors
      } else if (this.ncwellmap1style === 'pattern1') {
        getStyle = this.getPatternColors
      } else if (this.ncwellmap1style === 'pattern2') {
        getStyle = this.getPatternColors
      }
      return feature => {
        let selected = !!this.vtSelection[feature.get(this.vtIdProp)]
        let data = feature.getProperties()
        let variable = this.currentradiovariable1
        if (variable === 'ncwellwise_arsenic_med') {
          getStyle(data, this.arsenic_med_values, this.arsncolors, variable, 'ncwelllayer1')
        } else if (variable === 'ncwellwise_arsenic_mean') {
          getStyle(data, this.arsenic_mean_values, this.arsncolors, variable, 'ncwelllayer1')
        } else if (variable === 'ncwellwise_arsenic_prcast') {
          getStyle(data, this.arsenic_prcast_values, this.arsncolors, variable, 'ncwelllayer1')
        } else if (variable === 'ncwellwise_cadmium_med') {
          getStyle(data, this.cadmium_med_values, this.cadmcolors, variable, 'ncwelllayer1')
        } else if (variable === 'ncwellwise_cadmium_mean') {
          getStyle(data, this.cadmium_mean_values, this.cadmcolors, variable, 'ncwelllayer1')
        } else if (variable === 'ncwellwise_cadmium_prcast') {
          getStyle(data, this.cadmium_prcast_values, this.cadmcolors, variable, 'ncwelllayer1')
        } else if (variable === 'ncwellwise_lead_med') {
          getStyle(data, this.lead_med_values, this.leadcolors, variable, 'ncwelllayer1')
        } else if (variable === 'ncwellwise_lead_mean') {
          getStyle(data, this.lead_mean_values, this.leadcolors, variable, 'ncwelllayer1')
        } else if (variable === 'ncwellwise_lead_prcast') {
          getStyle(data, this.lead_prcast_values, this.leadcolors, variable, 'ncwelllayer1')
        } else if (variable === 'ncwellwise_manganese_med') {
          getStyle(data, this.manganese_med_values, this.mngncolors, variable, 'ncwelllayer1')
        } else if (variable === 'ncwellwise_manganese_mean') {
          getStyle(data, this.manganese_mean_values, this.mngncolors, variable, 'ncwelllayer1')
        } else if (variable === 'ncwellwise_manganese_prcast') {
          getStyle(data, this.manganese_prcast_values, this.mngncolors, variable, 'ncwelllayer1')
        }
        return [
          new Style({
            stroke: new Stroke({
              color: selected ? 'rgba(200,20,20,1.0)' : 'black',
              width: selected ? 5 : (this.zoom / 8.0)
            }),
            fill: new Fill({
              color: selected ? 'rgba(200,20,20,0.0)' : this.varcolor
            })
          })
        ]
      }
    },
    getacsStyle1: function () {
      let getStyle
      if (this.acsmap1style === 'nopattern') {
        getStyle = this.getColors
      } else if (this.acsmap1style === 'pattern1') {
        getStyle = this.getPatternColors
      } else if (this.acsmap1style === 'pattern2') {
        getStyle = this.getPatternColors
      }
      return feature => {
        let selected = !!this.vtSelection[feature.get(this.vtIdProp)]
        let data = feature.getProperties()
        let variable = this.currentacsvariable1
        getStyle(data, this.census_acs_values, this.acscolors, variable, 'acslayer1')
        return [
          new Style({
            stroke: new Stroke({
              color: selected ? 'rgba(200,20,20,1.0)' : 'black',
              width: selected ? 5 : (this.zoom / 8.0)
            }),
            fill: new Fill({
              color: selected ? 'rgba(200,20,20,0.0)' : this.varcolor
            })
          })
        ]
      }
    },
    getejscreenStyle1: function () {
      let getStyle
      if (this.ejsmap1style === 'nopattern') {
        getStyle = this.getColors
      } else if (this.ejsmap1style === 'pattern1') {
        getStyle = this.getPatternColors
      } else if (this.ejsmap1style === 'pattern2') {
        getStyle = this.getPatternColors
      }
      return feature => {
        let selected = !!this.vtSelection[feature.get(this.vtIdProp)]
        let data = feature.getProperties()
        let variable = this.currentejsvariable1
        if (variable === 'd_ldpnt_2') {
          getStyle(data, this.d_ldpnt_2_values, this.ejscolors, variable, 'ejslayer1')
        } else if (variable === 'd_dslpm_2') {
          getStyle(data, this.d_dslpm_2_values, this.ejscolors, variable, 'ejslayer1')
        } else if (variable === 'd_cancr_2') {
          getStyle(data, this.d_cancr_2_values, this.ejscolors, variable, 'ejslayer1')
        } else if (variable === 'd_resp_2') {
          getStyle(data, this.d_resp_2_values, this.ejscolors, variable, 'ejslayer1')
        } else if (variable === 'd_ptraf_2') {
          getStyle(data, this.d_ptraf_2_values, this.ejscolors, variable, 'ejslayer1')
        } else if (variable === 'd_pwdis_2') {
          getStyle(data, this.d_pwdis_2_values, this.ejscolors, variable, 'ejslayer1')
        } else if (variable === 'd_pnpl_2') {
          getStyle(data, this.d_pnpl_2_values, this.ejscolors, variable, 'ejslayer1')
        } else if (variable === 'd_prmp_2') {
          getStyle(data, this.d_prmp_2_values, this.ejscolors, variable, 'ejslayer1')
        } else if (variable === 'd_ptsdf_2') {
          getStyle(data, this.d_ptsdf_2_values, this.ejscolors, variable, 'ejslayer1')
        } else if (variable === 'd_ozone_2') {
          getStyle(data, this.d_ozone_2_values, this.ejscolors, variable, 'ejslayer1')
        } else if (variable === 'd_pm25_2') {
          getStyle(data, this.d_pm25_2_values, this.ejscolors, variable, 'ejslayer1')
        }
        return [
          new Style({
            stroke: new Stroke({
              color: selected ? 'rgba(200,20,20,1.0)' : 'black',
              width: selected ? 5 : (this.zoom / 8.0)
            }),
            fill: new Fill({
              color: selected ? 'rgba(200,20,20,0.0)' : this.varcolor
            })
          })
        ]
      }
    },
    getcovid19Style1: function () {
      return feature => {
        let selected = !!this.vtSelection[feature.get(this.vtIdProp)]
        let data = feature.getProperties()
        let variable = this.currentradiovariable1
        if (variable === 'cases') {
          this.getColors(data, this.covid_cases_values, this.covidcolors, variable, 'covidlayer1')
        } else if (variable === 'cases_per_10000_res') {
          this.getColors(data, this.covid_cases_per_10000_res_values, this.covidcolors, variable, 'covidlayer1')
        } else if (variable === 'cases_per_100000_res') {
          this.getColors(data, this.covid_cases_per_100000_res_values, this.covidcolors, variable, 'covidlayer1')
        } else if (variable === 'deaths') {
          this.getColors(data, this.covid_deaths_values, this.covidcolors, variable, 'covidlayer1')
        }
        return [
          new Style({
            stroke: new Stroke({
              color: selected ? 'rgba(200,20,20,1.0)' : 'black',
              width: selected ? 5 : (this.zoom / 8.0)
            }),
            fill: new Fill({
              color: selected ? 'rgba(200,20,20,0.0)' : this.varcolor
            })
          })
        ]
      }
    },
    getpretermStyle1: function () {
      let getStyle
      if (this.pretermmap1style === 'nopattern') {
        getStyle = this.getColors
      } else if (this.pretermmap1style === 'pattern1') {
        getStyle = this.getPatternColors
      } else if (this.pretermmap1style === 'pattern2') {
        getStyle = this.getPatternColors
      }
      return feature => {
        let selected = !!this.vtSelection[feature.get(this.vtIdProp)]
        let data = feature.getProperties()
        let variable = this.currentpretermvariable1
        if (this.currentpretermvariable1 === 'fc_calcega_mean_avg') {
          getStyle(data, this.ega_mean_avg_values, this.pretermcolors, variable, 'pretermlayer1')
        } else if (this.currentpretermvariable1 === 'fc_calcpreterm_percentage') {
          getStyle(data, this.preterm_percentage_values, this.pretermcolors, variable, 'pretermlayer1')
        } else if (this.currentpretermvariable1 === 'fc_clinega_mean_avg') {
          getStyle(data, this.ega_mean_avg_values, this.pretermcolors, variable, 'pretermlayer1')
        } else if (this.currentpretermvariable1 === 'fc_clinpreterm_percentage') {
          getStyle(data, this.preterm_percentage_values, this.pretermcolors, variable, 'pretermlayer1')
        } else if (this.currentpretermvariable1 === 'sc_calcega_mean_avg') {
          getStyle(data, this.ega_mean_avg_values, this.pretermcolors, variable, 'pretermlayer1')
        } else if (this.currentpretermvariable1 === 'sc_calcpreterm_percentage') {
          getStyle(data, this.preterm_percentage_values, this.pretermcolors, variable, 'pretermlayer1')
        } else if (this.currentpretermvariable1 === 'sc_clinega_mean_avg') {
          getStyle(data, this.ega_mean_avg_values, this.pretermcolors, variable, 'pretermlayer1')
        } else if (this.currentpretermvariable1 === 'sc_clinpreterm_percentage') {
          getStyle(data, this.preterm_percentage_values, this.pretermcolors, variable, 'pretermlayer1')
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
    getncwellwiseStyle2: function () {
      let getStyle
      if (this.ncwellmap2style === 'nopattern') {
        getStyle = this.getColors
      } else if (this.ncwellmap2style === 'pattern1') {
        getStyle = this.getPatternColors
      } else if (this.ncwellmap2style === 'pattern2') {
        getStyle = this.getPatternColors
      }
      return feature => {
        let selected = !!this.vtSelection[feature.get(this.vtIdProp)]
        let data = feature.getProperties()
        let variable = this.currentradiovariable2
        if (variable === 'ncwellwise_arsenic_med') {
          getStyle(data, this.arsenic_med_values, this.arsncolors, variable, 'ncwelllayer2')
        } else if (variable === 'ncwellwise_arsenic_mean') {
          getStyle(data, this.arsenic_mean_values, this.arsncolors, variable, 'ncwelllayer2')
        } else if (variable === 'ncwellwise_arsenic_prcast') {
          getStyle(data, this.arsenic_prcast_values, this.arsncolors, variable, 'ncwelllayer2')
        } else if (variable === 'ncwellwise_cadmium_med') {
          getStyle(data, this.cadmium_med_values, this.cadmcolors, variable, 'ncwelllayer2')
        } else if (variable === 'ncwellwise_cadmium_mean') {
          getStyle(data, this.cadmium_mean_values, this.cadmcolors, variable, 'ncwelllayer2')
        } else if (variable === 'ncwellwise_cadmium_prcast') {
          getStyle(data, this.cadmium_prcast_values, this.cadmcolors, variable, 'ncwelllayer2')
        } else if (variable === 'ncwellwise_lead_med') {
          getStyle(data, this.lead_med_values, this.leadcolors, variable, 'ncwelllayer2')
        } else if (variable === 'ncwellwise_lead_mean') {
          getStyle(data, this.lead_mean_values, this.leadcolors, variable, 'ncwelllayer2')
        } else if (variable === 'ncwellwise_lead_prcast') {
          getStyle(data, this.lead_prcast_values, this.leadcolors, variable, 'ncwelllayer2')
        } else if (variable === 'ncwellwise_manganese_med') {
          getStyle(data, this.manganese_med_values, this.mngncolors, variable, 'ncwelllayer2')
        } else if (variable === 'ncwellwise_manganese_mean') {
          getStyle(data, this.manganese_mean_values, this.mngncolors, variable, 'ncwelllayer2')
        } else if (variable === 'ncwellwise_manganese_prcast') {
          getStyle(data, this.manganese_prcast_values, this.mngncolors, variable, 'ncwelllayer2')
        }
        return [
          new Style({
            stroke: new Stroke({
              color: selected ? 'rgba(200,20,20,1.0)' : 'black',
              width: selected ? 5 : (this.zoom / 8.0)
            }),
            fill: new Fill({
              color: selected ? 'rgba(200,20,20,0.0)' : this.varcolor
            })
          })
        ]
      }
    },
    getacsStyle2: function () {
      let getStyle
      if (this.acsmap2style === 'nopattern') {
        getStyle = this.getColors
      } else if (this.acsmap2style === 'pattern1') {
        getStyle = this.getPatternColors
      } else if (this.acsmap2style === 'pattern2') {
        getStyle = this.getPatternColors
      }
      return feature => {
        let selected = !!this.vtSelection[feature.get(this.vtIdProp)]
        let data = feature.getProperties()
        let variable = this.currentacsvariable2
        getStyle(data, this.census_acs_values, this.acscolors, variable, 'acslayer2')
        return [
          new Style({
            stroke: new Stroke({
              color: selected ? 'rgba(200,20,20,1.0)' : 'black',
              width: selected ? 5 : (this.zoom / 8.0)
            }),
            fill: new Fill({
              color: selected ? 'rgba(200,20,20,0.0)' : this.varcolor
            })
          })
        ]
      }
    },
    getejscreenStyle2: function () {
      let getStyle
      if (this.ejsmap2style === 'nopattern') {
        getStyle = this.getColors
      } else if (this.ejsmap2style === 'pattern1') {
        getStyle = this.getPatternColors
      } else if (this.ejsmap2style === 'pattern2') {
        getStyle = this.getPatternColors
      }
      return feature => {
        let selected = !!this.vtSelection[feature.get(this.vtIdProp)]
        let data = feature.getProperties()
        let variable = this.currentejsvariable2
        if (variable === 'd_ldpnt_2') {
          getStyle(data, this.d_ldpnt_2_values, this.ejscolors, variable, 'ejslayer2')
        } else if (variable === 'd_dslpm_2') {
          getStyle(data, this.d_dslpm_2_values, this.ejscolors, variable, 'ejslayer2')
        } else if (variable === 'd_cancr_2') {
          getStyle(data, this.d_cancr_2_values, this.ejscolors, variable, 'ejslayer2')
        } else if (variable === 'd_resp_2') {
          getStyle(data, this.d_resp_2_values, this.ejscolors, variable, 'ejslayer2')
        } else if (variable === 'd_ptraf_2') {
          getStyle(data, this.d_ptraf_2_values, this.ejscolors, variable, 'ejslayer2')
        } else if (variable === 'd_pwdis_2') {
          getStyle(data, this.d_pwdis_2_values, this.ejscolors, variable, 'ejslayer2')
        } else if (variable === 'd_pnpl_2') {
          getStyle(data, this.d_pnpl_2_values, this.ejscolors, variable, 'ejslayer2')
        } else if (variable === 'd_prmp_2') {
          getStyle(data, this.d_prmp_2_values, this.ejscolors, variable, 'ejslayer2')
        } else if (variable === 'd_ptsdf_2') {
          getStyle(data, this.d_ptsdf_2_values, this.ejscolors, variable, 'ejslayer2')
        } else if (variable === 'd_ozone_2') {
          getStyle(data, this.d_ozone_2_values, this.ejscolors, variable, 'ejslayer2')
        } else if (variable === 'd_pm25_2') {
          getStyle(data, this.d_pm25_2_values, this.ejscolors, variable, 'ejslayer2')
        }
        return [
          new Style({
            stroke: new Stroke({
              color: selected ? 'rgba(200,20,20,1.0)' : 'black',
              width: selected ? 5 : (this.zoom / 8.0)
            }),
            fill: new Fill({
              color: selected ? 'rgba(200,20,20,0.0)' : this.varcolor
            })
          })
        ]
      }
    },
    getcovid19Style2: function () {
      return feature => {
        let selected = !!this.vtSelection[feature.get(this.vtIdProp)]
        let data = feature.getProperties()
        let variable = this.currentradiovariable2
        if (variable === 'cases') {
          this.getColors(data, this.covid_cases_values, this.covidcolors, variable, 'covidlayer2')
        } else if (variable === 'cases_per_10000_res') {
          this.getColors(data, this.covid_cases_per_10000_res_values, this.covidcolors, variable, 'covidlayer2')
        } else if (variable === 'cases_per_100000_res') {
          this.getColors(data, this.covid_cases_per_100000_res_values, this.covidcolors, variable, 'covidlayer2')
        } else if (variable === 'deaths') {
          this.getColors(data, this.covid_deaths_values, this.covidcolors, variable, 'covidlayer2')
        }
        return [
          new Style({
            stroke: new Stroke({
              color: selected ? 'rgba(200,20,20,1.0)' : 'black',
              width: selected ? 5 : (this.zoom / 8.0)
            }),
            fill: new Fill({
              color: selected ? 'rgba(200,20,20,0.0)' : this.varcolor
            })
          })
        ]
      }
    },
    getpretermStyle2: function () {
      let getStyle
      if (this.pretermmap2style === 'nopattern') {
        getStyle = this.getColors
      } else if (this.pretermmap2style === 'pattern1') {
        getStyle = this.getPatternColors
      } else if (this.pretermmap2style === 'pattern2') {
        getStyle = this.getPatternColors
      }
      return feature => {
        let selected = !!this.vtSelection[feature.get(this.vtIdProp)]
        let data = feature.getProperties()
        let variable = this.currentpretermvariable2
        if (this.currentpretermvariable2 === 'fc_calcega_mean_avg') {
          getStyle(data, this.ega_mean_avg_values, this.pretermcolors, variable, 'pretermlayer2')
        } else if (this.currentpretermvariable2 === 'fc_calcpreterm_percentage') {
          getStyle(data, this.preterm_percentage_values, this.pretermcolors, variable, 'pretermlayer2')
        } else if (this.currentpretermvariable2 === 'fc_clinega_mean_avg') {
          getStyle(data, this.ega_mean_avg_values, this.pretermcolors, variable, 'pretermlayer2')
        } else if (this.currentpretermvariable2 === 'fc_clinpreterm_percentage') {
          getStyle(data, this.preterm_percentage_values, this.pretermcolors, variable, 'pretermlayer2')
        } else if (this.currentpretermvariable2 === 'sc_calcega_mean_avg') {
          getStyle(data, this.ega_mean_avg_values, this.pretermcolors, variable, 'pretermlayer2')
        } else if (this.currentpretermvariable2 === 'sc_calcpreterm_percentage') {
          getStyle(data, this.preterm_percentage_values, this.pretermcolors, variable, 'pretermlayer2')
        } else if (this.currentpretermvariable2 === 'sc_clinega_mean_avg') {
          getStyle(data, this.ega_mean_avg_values, this.pretermcolors, variable, 'pretermlayer2')
        } else if (this.currentpretermvariable2 === 'sc_clinpreterm_percentage') {
          getStyle(data, this.preterm_percentage_values, this.pretermcolors, variable, 'pretermlayer2')
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
      // let zoom = this.getZoom2() // this.zoom
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
      // let zoom = this.getZoom2() // this.zoom
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
    getNCWellwiseLayer1ID: function () {
      return 'ncwellwise_layer1'
    },
    getACSCensusLayer1ID: function () {
      return 'acs_census_layer1'
    },
    getEJScreenLayer1ID: function () {
      return 'ejscreen_layer1'
    },
    getCovid19Layer1ID: function () {
      return 'covid19_layer1'
    },
    getPreTermLayer1ID: function () {
      return 'preterm_layer1'
    },
    getNCWellwiseLayer2ID: function () {
      return 'ncwellwise_layer2'
    },
    getACSCensusLayer2ID: function () {
      return 'acs_census_layer2'
    },
    getEJScreenLayer2ID: function () {
      return 'ejscreen_layer2'
    },
    getCovid19Layer2ID: function () {
      return 'covid19_layer2'
    },
    getPreTermLayer2ID: function () {
      return 'preterm_layer2'
    },
    onMapMounted: function (map1) {
      // now ol.Map instance is ready and we can work with it directly
      this.$refs.map1.$map.getControls().extend([
        new ScaleLine({
          target: 'Scale1Target'
        }),
        /* new OverviewMap({
          collapsed: false,
          collapsible: true,
          target: 'OverviewMap1Target'
        }), */
        new Zoom({
          target: 'Zoom1Target'
        }),
        new Attribution({
          collapsed: false,
          collapsible: false,
          target: 'Attribution1Target'
        })
      ])
      this.$refs.map2.$map.getControls().extend([
        new Zoom({
          target: 'Zoom2Target'
        })
        /* new ScaleLine({
          target: 'Scale2Target'
        }),
        new OverviewMap({
          collapsed: false,
          collapsible: true,
          target: 'OverviewMap2Target'
        }),
        new Attribution({
          collapsed: false,
          collapsible: false,
          target: 'Attribution2Target'
        }) */
      ])
    },
    // base layers
    showBaseLayer1: function () {
      let layer = this.baseLayers1.find(layer => layer.visible)
      if (layer != null) {
        layer.visible = false
      }

      layer = this.baseLayers1.find(layer => layer.name === this.baselayer1)
      if (layer != null) {
        layer.visible = true
      }
    },
    // base layers
    showBaseLayer2: function () {
      let layer = this.baseLayers2.find(layer => layer.visible)
      if (layer != null) {
        layer.visible = false
      }

      layer = this.baseLayers2.find(layer => layer.name === this.baselayer2)
      if (layer != null) {
        layer.visible = true
      }
    },
    showMap1PanelToggleLayer: function (variable) {
      if (variable === 'nccounties') {
        if (this.cntlayer1 === undefined) {
          this.cntlayer1 = this.layers1[5]
        }
        if (this.ncCountiesModel1 === 'Selected') {
          this.cntlayer1.visible = true
        } else if (this.ncCountiesModel1 === 'Not Selected') {
          this.cntlayer1.visible = false
        }
      } else if (variable === 'percent_below_poverty_level') {
        if (this.acslayer1 === undefined) {
          this.acslayer1 = this.layers1[1]
        }
        if (this.povertyModel1 === 'Selected') {
          this.acslayer1.visible = true
          this.currentacsvariable1 = variable
        } else if (this.povertyModel1 === 'Not Selected') {
          this.acslayer1.visible = false
        }
      } else if (variable === 'american_indian_and_alaska_native_alone') {
        if (this.acslayer1 === undefined) {
          this.acslayer1 = this.layers1[1]
        }
        if (this.nativeModel1 === 'Selected') {
          this.acslayer1.visible = true
          this.currentacsvariable1 = variable
        } else if (this.nativeModel1 === 'Not Selected') {
          this.acslayer1.visible = false
        }
      } else if (variable === 'asian_alone') {
        if (this.acslayer1 === undefined) {
          this.acslayer1 = this.layers1[1]
        }
        if (this.asianModel1 === 'Selected') {
          this.acslayer1.visible = true
          this.currentacsvariable1 = variable
        } else if (this.asianModel1 === 'Not Selected') {
          this.acslayer1.visible = false
        }
      } else if (variable === 'black_or_african_american_alone') {
        if (this.acslayer1 === undefined) {
          this.acslayer1 = this.layers1[1]
        }
        if (this.blackModel1 === 'Selected') {
          this.acslayer1.visible = true
          this.currentacsvariable1 = variable
        } else if (this.blackModel1 === 'Not Selected') {
          this.acslayer1.visible = false
        }
      } else if (variable === 'native_hawaiian_and_other_pacific_islander_alone') {
        if (this.acslayer1 === undefined) {
          this.acslayer1 = this.layers1[1]
        }
        if (this.polyModel1 === 'Selected') {
          this.acslayer1.visible = true
          this.currentacsvariable1 = variable
        } else if (this.polyModel1 === 'Not Selected') {
          this.acslayer1.visible = false
        }
      } else if (variable === 'white_alone') {
        if (this.acslayer1 === undefined) {
          this.acslayer1 = this.layers1[1]
        }
        if (this.whiteModel1 === 'Selected') {
          this.acslayer1.visible = true
          this.currentacsvariable1 = variable
        } else if (this.whiteModel1 === 'Not Selected') {
          this.acslayer1.visible = false
        }
      } else if (variable === 'two_or_more_races') {
        if (this.acslayer1 === undefined) {
          this.acslayer1 = this.layers1[1]
        }
        if (this.tworacesModel1 === 'Selected') {
          this.acslayer1.visible = true
          this.currentacsvariable1 = variable
        } else if (this.tworacesModel1 === 'Not Selected') {
          this.acslayer1.visible = false
        }
      } else if (variable === 'hispanic_or_latino_of_any_race') {
        if (this.acslayer1 === undefined) {
          this.acslayer1 = this.layers1[1]
        }
        if (this.hispModel1 === 'Selected') {
          this.acslayer1.visible = true
          this.currentacsvariable1 = variable
        } else if (this.hispModel1 === 'Not Selected') {
          this.acslayer1.visible = false
        }
      } else if (variable === 'not_hispanic_or_latino') {
        if (this.acslayer1 === undefined) {
          this.acslayer1 = this.layers1[1]
        }
        if (this.nothispModel1 === 'Selected') {
          this.acslayer1.visible = true
          this.currentacsvariable1 = variable
        } else if (this.nothispModel1 === 'Not Selected') {
          this.acslayer1.visible = false
        }
      } else if (variable === 'speak_a_language_other_than_english') {
        if (this.acslayer1 === undefined) {
          this.acslayer1 = this.layers1[1]
        }
        if (this.langModel1 === 'Selected') {
          this.acslayer1.visible = true
          this.currentacsvariable1 = variable
        } else if (this.langModel1 === 'Not Selected') {
          this.acslayer1.visible = false
        }
      } else if (variable === 'd_ldpnt_2') {
        if (this.ejslayer1 === undefined) {
          this.ejslayer1 = this.layers1[2]
        }
        if (this.d_ldpnt_2Model1 === 'Selected') {
          this.ejslayer1.visible = true
          this.currentejsvariable1 = variable
        } else if (this.d_ldpnt_2Model1 === 'Not Selected') {
          this.ejslayer1.visible = false
        }
      } else if (variable === 'd_dslpm_2') {
        if (this.ejslayer1 === undefined) {
          this.ejslayer1 = this.layers1[2]
        }
        if (this.d_dslpm_2Model1 === 'Selected') {
          this.ejslayer1.visible = true
          this.currentejsvariable1 = variable
        } else if (this.d_dslpm_2Model1 === 'Not Selected') {
          this.ejslayer1.visible = false
        }
      } else if (variable === 'd_cancr_2') {
        if (this.ejslayer1 === undefined) {
          this.ejslayer1 = this.layers1[2]
        }
        if (this.d_cancr_2Model1 === 'Selected') {
          this.ejslayer1.visible = true
          this.currentejsvariable1 = variable
        } else if (this.d_cancr_2Model1 === 'Not Selected') {
          this.ejslayer1.visible = false
        }
      } else if (variable === 'd_resp_2') {
        if (this.ejslayer1 === undefined) {
          this.ejslayer1 = this.layers1[2]
        }
        if (this.d_resp_2Model1 === 'Selected') {
          this.ejslayer1.visible = true
          this.currentejsvariable1 = variable
        } else if (this.d_resp_2Model1 === 'Not Selected') {
          this.ejslayer1.visible = false
        }
      } else if (variable === 'd_ptraf_2') {
        if (this.ejslayer1 === undefined) {
          this.ejslayer1 = this.layers1[2]
        }
        if (this.d_ptraf_2Model1 === 'Selected') {
          this.ejslayer1.visible = true
          this.currentejsvariable1 = variable
        } else if (this.d_ptraf_2Model1 === 'Not Selected') {
          this.ejslayer1.visible = false
        }
      } else if (variable === 'd_pwdis_2') {
        if (this.ejslayer1 === undefined) {
          this.ejslayer1 = this.layers1[2]
        }
        if (this.d_pwdis_2Model1 === 'Selected') {
          this.ejslayer1.visible = true
          this.currentejsvariable1 = variable
        } else if (this.d_pwdis_2Model1 === 'Not Selected') {
          this.ejslayer1.visible = false
        }
      } else if (variable === 'd_pnpl_2') {
        if (this.ejslayer1 === undefined) {
          this.ejslayer1 = this.layers1[2]
        }
        if (this.d_pnpl_2Model1 === 'Selected') {
          this.ejslayer1.visible = true
          this.currentejsvariable1 = variable
        } else if (this.d_pnpl_2Model1 === 'Not Selected') {
          this.ejslayer1.visible = false
        }
      } else if (variable === 'd_prmp_2') {
        if (this.ejslayer1 === undefined) {
          this.ejslayer1 = this.layers1[2]
        }
        if (this.d_prmp_2Model1 === 'Selected') {
          this.ejslayer1.visible = true
          this.currentejsvariable1 = variable
        } else if (this.d_prmp_2Model1 === 'Not Selected') {
          this.ejslayer1.visible = false
        }
      } else if (variable === 'd_ptsdf_2') {
        if (this.ejslayer1 === undefined) {
          this.ejslayer1 = this.layers1[2]
        }
        if (this.d_ptsdf_2Model1 === 'Selected') {
          this.ejslayer1.visible = true
          this.currentejsvariable1 = variable
        } else if (this.d_ptsdf_2Model1 === 'Not Selected') {
          this.ejslayer1.visible = false
        }
      } else if (variable === 'd_ozone_2') {
        if (this.ejslayer1 === undefined) {
          this.ejslayer1 = this.layers1[2]
        }
        if (this.d_ozone_2Model1 === 'Selected') {
          this.ejslayer1.visible = true
          this.currentejsvariable1 = variable
        } else if (this.d_ozone_2Model1 === 'Not Selected') {
          this.ejslayer1.visible = false
        }
      } else if (variable === 'd_pm25_2') {
        if (this.ejslayer1 === undefined) {
          this.ejslayer1 = this.layers1[2]
        }
        if (this.d_pm25_2Model1 === 'Selected') {
          this.ejslayer1.visible = true
          this.currentejsvariable1 = variable
        } else if (this.d_pm25_2Model1 === 'Not Selected') {
          this.ejslayer1.visible = false
        }
      } else if (variable === 'fc_calcega_mean_avg') {
        if (this.pretermlayer1 === undefined) {
          this.pretermlayer1 = this.layers1[4]
        }
        if (this.fc_calcega_mean_avgModel1 === 'Selected') {
          this.pretermlayer1.visible = true
          this.currentpretermvariable1 = variable
        } else if (this.fc_calcega_mean_avgModel1 === 'Not Selected') {
          this.pretermlayer1.visible = false
        }
      } else if (variable === 'fc_clinega_mean_avg') {
        if (this.pretermlayer1 === undefined) {
          this.pretermlayer1 = this.layers1[4]
        }
        if (this.fc_clinega_mean_avgModel1 === 'Selected') {
          this.pretermlayer1.visible = true
          this.currentpretermvariable1 = variable
        } else if (this.fc_clinega_mean_avgModel1 === 'Not Selected') {
          this.pretermlayer1.visible = false
        }
      } else if (variable === 'sc_calcega_mean_avg') {
        if (this.pretermlayer1 === undefined) {
          this.pretermlayer1 = this.layers1[4]
        }
        if (this.sc_calcega_mean_avgModel1 === 'Selected') {
          this.pretermlayer1.visible = true
          this.currentpretermvariable1 = variable
        } else if (this.sc_calcega_mean_avgModel1 === 'Not Selected') {
          this.pretermlayer1.visible = false
        }
      } else if (variable === 'sc_clinega_mean_avg') {
        if (this.pretermlayer1 === undefined) {
          this.pretermlayer1 = this.layers1[4]
        }
        if (this.sc_clinega_mean_avgModel1 === 'Selected') {
          this.pretermlayer1.visible = true
          this.currentpretermvariable1 = variable
        } else if (this.sc_clinega_mean_avgModel1 === 'Not Selected') {
          this.pretermlayer1.visible = false
        }
      } else if (variable === 'fc_calcpreterm_percentage') {
        if (this.pretermlayer1 === undefined) {
          this.pretermlayer1 = this.layers1[4]
        }
        if (this.fc_calcpreterm_percentageModel1 === 'Selected') {
          this.pretermlayer1.visible = true
          this.currentpretermvariable1 = variable
        } else if (this.fc_calcpreterm_percentageModel1 === 'Not Selected') {
          this.pretermlayer1.visible = false
        }
      } else if (variable === 'fc_clinpreterm_percentage') {
        if (this.pretermlayer1 === undefined) {
          this.pretermlayer1 = this.layers1[4]
        }
        if (this.fc_clinpreterm_percentageModel1 === 'Selected') {
          this.pretermlayer1.visible = true
          this.currentpretermvariable1 = variable
        } else if (this.fc_clinpreterm_percentageModel1 === 'Not Selected') {
          this.pretermlayer1.visible = false
        }
      } else if (variable === 'sc_calcpreterm_percentage') {
        if (this.pretermlayer1 === undefined) {
          this.pretermlayer1 = this.layers1[4]
        }
        if (this.sc_calcpreterm_percentageModel1 === 'Selected') {
          this.pretermlayer1.visible = true
          this.currentpretermvariable1 = variable
        } else if (this.sc_calcpreterm_percentageModel1 === 'Not Selected') {
          this.pretermlayer1.visible = false
        }
      } else if (variable === 'sc_clinpreterm_percentage') {
        if (this.pretermlayer1 === undefined) {
          this.pretermlayer1 = this.layers1[4]
        }
        if (this.sc_clinpreterm_percentageModel1 === 'Selected') {
          this.pretermlayer1.visible = true
          this.currentpretermvariable1 = variable
        } else if (this.sc_clinpreterm_percentageModel1 === 'Not Selected') {
          this.pretermlayer1.visible = false
        }
      }
    },
    showMap2PanelToggleLayer: function (variable) {
      if (variable === 'nccounties') {
        if (this.cntlayer2 === undefined) {
          this.cntlayer2 = this.layers2[5]
        }
        if (this.ncCountiesModel2 === 'Selected') {
          this.cntlayer2.visible = true
        } else if (this.ncCountiesModel2 === 'Not Selected') {
          this.cntlayer2.visible = false
        }
      } else if (variable === 'percent_below_poverty_level') {
        if (this.acslayer2 === undefined) {
          this.acslayer2 = this.layers2[1]
        }
        if (this.povertyModel2 === 'Selected') {
          this.acslayer2.visible = true
          this.currentacsvariable2 = variable
        } else if (this.povertyModel2 === 'Not Selected') {
          this.acslayer2.visible = false
        }
      } else if (variable === 'american_indian_and_alaska_native_alone') {
        if (this.acslayer2 === undefined) {
          this.acslayer2 = this.layers2[1]
        }
        if (this.nativeModel2 === 'Selected') {
          this.acslayer2.visible = true
          this.currentacsvariable2 = variable
        } else if (this.nativeModel2 === 'Not Selected') {
          this.acslayer2.visible = false
        }
      } else if (variable === 'asian_alone') {
        if (this.acslayer2 === undefined) {
          this.acslayer2 = this.layers2[1]
        }
        if (this.asianModel2 === 'Selected') {
          this.acslayer2.visible = true
          this.currentacsvariable2 = variable
        } else if (this.asianModel2 === 'Not Selected') {
          this.acslayer2.visible = false
        }
      } else if (variable === 'black_or_african_american_alone') {
        if (this.acslayer2 === undefined) {
          this.acslayer2 = this.layers2[1]
        }
        if (this.blackModel2 === 'Selected') {
          this.acslayer2.visible = true
          this.currentacsvariable2 = variable
        } else if (this.blackModel2 === 'Not Selected') {
          this.acslayer2.visible = false
        }
      } else if (variable === 'native_hawaiian_and_other_pacific_islander_alone') {
        if (this.acslayer2 === undefined) {
          this.acslayer2 = this.layers2[1]
        }
        if (this.polyModel2 === 'Selected') {
          this.acslayer2.visible = true
          this.currentacsvariable2 = variable
        } else if (this.polyModel2 === 'Not Selected') {
          this.acslayer2.visible = false
        }
      } else if (variable === 'white_alone') {
        if (this.acslayer2 === undefined) {
          this.acslayer2 = this.layers2[1]
        }
        if (this.whiteModel2 === 'Selected') {
          this.acslayer2.visible = true
          this.currentacsvariable2 = variable
        } else if (this.whiteModel2 === 'Not Selected') {
          this.acslayer2.visible = false
        }
      } else if (variable === 'two_or_more_races') {
        if (this.acslayer2 === undefined) {
          this.acslayer2 = this.layers2[1]
        }
        if (this.tworacesModel2 === 'Selected') {
          this.acslayer2.visible = true
          this.currentacsvariable2 = variable
        } else if (this.tworacesModel2 === 'Not Selected') {
          this.acslayer2.visible = false
        }
      } else if (variable === 'hispanic_or_latino_of_any_race') {
        if (this.acslayer2 === undefined) {
          this.acslayer2 = this.layers2[1]
        }
        if (this.hispModel2 === 'Selected') {
          this.acslayer2.visible = true
          this.currentacsvariable2 = variable
        } else if (this.hispModel2 === 'Not Selected') {
          this.acslayer2.visible = false
        }
      } else if (variable === 'not_hispanic_or_latino') {
        if (this.acslayer2 === undefined) {
          this.acslayer2 = this.layers2[1]
        }
        if (this.nothispModel2 === 'Selected') {
          this.acslayer2.visible = true
          this.currentacsvariable2 = variable
        } else if (this.nothispModel2 === 'Not Selected') {
          this.acslayer2.visible = false
        }
      } else if (variable === 'speak_a_language_other_than_english') {
        if (this.acslayer2 === undefined) {
          this.acslayer2 = this.layers2[1]
        }
        if (this.langModel2 === 'Selected') {
          this.acslayer2.visible = true
          this.currentacsvariable2 = variable
        } else if (this.langModel2 === 'Not Selected') {
          this.acslayer2.visible = false
        }
      } else if (variable === 'd_ldpnt_2') {
        if (this.ejslayer2 === undefined) {
          this.ejslayer2 = this.layers2[2]
        }
        if (this.d_ldpnt_2Model2 === 'Selected') {
          this.ejslayer2.visible = true
          this.currentejsvariable2 = variable
        } else if (this.d_ldpnt_2Model2 === 'Not Selected') {
          this.ejslayer2.visible = false
        }
      } else if (variable === 'd_dslpm_2') {
        if (this.ejslayer2 === undefined) {
          this.ejslayer2 = this.layers2[2]
        }
        if (this.d_dslpm_2Model2 === 'Selected') {
          this.ejslayer2.visible = true
          this.currentejsvariable2 = variable
        } else if (this.d_dslpm_2Model2 === 'Not Selected') {
          this.ejslayer2.visible = false
        }
      } else if (variable === 'd_cancr_2') {
        if (this.ejslayer2 === undefined) {
          this.ejslayer2 = this.layers2[2]
        }
        if (this.d_cancr_2Model2 === 'Selected') {
          this.ejslayer2.visible = true
          this.currentejsvariable2 = variable
        } else if (this.d_cancr_2Model2 === 'Not Selected') {
          this.ejslayer2.visible = false
        }
      } else if (variable === 'd_resp_2') {
        if (this.ejslayer2 === undefined) {
          this.ejslayer2 = this.layers2[2]
        }
        if (this.d_resp_2Model2 === 'Selected') {
          this.ejslayer2.visible = true
          this.currentejsvariable2 = variable
        } else if (this.d_resp_2Model2 === 'Not Selected') {
          this.ejslayer2.visible = false
        }
      } else if (variable === 'd_ptraf_2') {
        if (this.ejslayer2 === undefined) {
          this.ejslayer2 = this.layers2[2]
        }
        if (this.d_ptraf_2Model2 === 'Selected') {
          this.ejslayer2.visible = true
          this.currentejsvariable2 = variable
        } else if (this.d_ptraf_2Model2 === 'Not Selected') {
          this.ejslayer2.visible = false
        }
      } else if (variable === 'd_pwdis_2') {
        if (this.ejslayer2 === undefined) {
          this.ejslayer2 = this.layers2[2]
        }
        if (this.d_pwdis_2Model2 === 'Selected') {
          this.ejslayer2.visible = true
          this.currentejsvariable2 = variable
        } else if (this.d_pwdis_2Model2 === 'Not Selected') {
          this.ejslayer2.visible = false
        }
      } else if (variable === 'd_pnpl_2') {
        if (this.ejslayer2 === undefined) {
          this.ejslayer2 = this.layers2[2]
        }
        if (this.d_pnpl_2Model2 === 'Selected') {
          this.ejslayer2.visible = true
          this.currentejsvariable2 = variable
        } else if (this.d_pnpl_2Model2 === 'Not Selected') {
          this.ejslayer2.visible = false
        }
      } else if (variable === 'd_prmp_2') {
        if (this.ejslayer2 === undefined) {
          this.ejslayer2 = this.layers2[2]
        }
        if (this.d_prmp_2Model2 === 'Selected') {
          this.ejslayer2.visible = true
          this.currentejsvariable2 = variable
        } else if (this.d_prmp_2Model2 === 'Not Selected') {
          this.ejslayer2.visible = false
        }
      } else if (variable === 'd_ptsdf_2') {
        if (this.ejslayer2 === undefined) {
          this.ejslayer2 = this.layers2[2]
        }
        if (this.d_ptsdf_2Model2 === 'Selected') {
          this.ejslayer2.visible = true
          this.currentejsvariable2 = variable
        } else if (this.d_ptsdf_2Model2 === 'Not Selected') {
          this.ejslayer2.visible = false
        }
      } else if (variable === 'd_ozone_2') {
        if (this.ejslayer2 === undefined) {
          this.ejslayer2 = this.layers2[2]
        }
        if (this.d_ozone_2Model2 === 'Selected') {
          this.ejslayer2.visible = true
          this.currentejsvariable2 = variable
        } else if (this.d_ozone_2Model2 === 'Not Selected') {
          this.ejslayer2.visible = false
        }
      } else if (variable === 'd_pm25_2') {
        if (this.ejslayer2 === undefined) {
          this.ejslayer2 = this.layers2[2]
        }
        if (this.d_pm25_2Model2 === 'Selected') {
          this.ejslayer2.visible = true
          this.currentejsvariable2 = variable
        } else if (this.d_pm25_2Model2 === 'Not Selected') {
          this.ejslayer2.visible = false
        }
      } else if (variable === 'fc_calcega_mean_avg') {
        if (this.pretermlayer2 === undefined) {
          this.pretermlayer2 = this.layers2[4]
        }
        if (this.fc_calcega_mean_avgModel2 === 'Selected') {
          this.pretermlayer2.visible = true
          this.currentpretermvariable2 = variable
        } else if (this.fc_calcega_mean_avgModel2 === 'Not Selected') {
          this.pretermlayer2.visible = false
        }
      } else if (variable === 'fc_clinega_mean_avg') {
        if (this.pretermlayer2 === undefined) {
          this.pretermlayer2 = this.layers2[4]
        }
        if (this.fc_clinega_mean_avgModel2 === 'Selected') {
          this.pretermlayer2.visible = true
          this.currentpretermvariable2 = variable
        } else if (this.fc_clinega_mean_avgModel2 === 'Not Selected') {
          this.pretermlayer2.visible = false
        }
      } else if (variable === 'sc_calcega_mean_avg') {
        if (this.pretermlayer2 === undefined) {
          this.pretermlayer2 = this.layers2[4]
        }
        if (this.sc_calcega_mean_avgModel2 === 'Selected') {
          this.pretermlayer2.visible = true
          this.currentpretermvariable2 = variable
        } else if (this.sc_calcega_mean_avgModel2 === 'Not Selected') {
          this.pretermlayer2.visible = false
        }
      } else if (variable === 'sc_clinega_mean_avg') {
        if (this.pretermlayer2 === undefined) {
          this.pretermlayer2 = this.layers2[4]
        }
        if (this.sc_clinega_mean_avgModel2 === 'Selected') {
          this.pretermlayer2.visible = true
          this.currentpretermvariable2 = variable
        } else if (this.sc_clinega_mean_avgModel2 === 'Not Selected') {
          this.pretermlayer2.visible = false
        }
      } else if (variable === 'fc_calcpreterm_percentage') {
        if (this.pretermlayer2 === undefined) {
          this.pretermlayer2 = this.layers2[4]
        }
        if (this.fc_calcpreterm_percentageModel2 === 'Selected') {
          this.pretermlayer2.visible = true
          this.currentpretermvariable2 = variable
        } else if (this.fc_calcpreterm_percentageModel2 === 'Not Selected') {
          this.pretermlayer2.visible = false
        }
      } else if (variable === 'fc_clinpreterm_percentage') {
        if (this.pretermlayer2 === undefined) {
          this.pretermlayer2 = this.layers2[4]
        }
        if (this.fc_clinpreterm_percentageModel2 === 'Selected') {
          this.pretermlayer2.visible = true
          this.currentpretermvariable2 = variable
        } else if (this.fc_clinpreterm_percentageModel2 === 'Not Selected') {
          this.pretermlayer2.visible = false
        }
      } else if (variable === 'sc_calcpreterm_percentage') {
        if (this.pretermlayer2 === undefined) {
          this.pretermlayer2 = this.layers2[4]
        }
        if (this.sc_calcpreterm_percentageModel2 === 'Selected') {
          this.pretermlayer2.visible = true
          this.currentpretermvariable2 = variable
        } else if (this.sc_calcpreterm_percentageModel2 === 'Not Selected') {
          this.pretermlayer2.visible = false
        }
      } else if (variable === 'sc_clinpreterm_percentage') {
        if (this.pretermlayer2 === undefined) {
          this.pretermlayer2 = this.layers2[4]
        }
        if (this.sc_clinpreterm_percentageModel2 === 'Selected') {
          this.pretermlayer2.visible = true
          this.currentpretermvariable2 = variable
        } else if (this.sc_clinpreterm_percentageModel2 === 'Not Selected') {
          this.pretermlayer2.visible = false
        }
      }
    },
    showMap1PanelRadioLayer: function () {
      let layer = this.layers1.find(layer => layer.visible)

      if (layer != null) {
        layer.visible = false
      }

      var i
      if (this.currentradiovariable1 === 'ncwellwise_arsenic_med') {
        layer = this.layers1.find(layer => layer.id === 'ncwellwise_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentradiovariable1 === 'ncwellwise_arsenic_mean') {
        layer = this.layers1.find(layer => layer.id === 'ncwellwise_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentradiovariable1 === 'ncwellwise_arsenic_prcast') {
        layer = this.layers1.find(layer => layer.id === 'ncwellwise_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentradiovariable1 === 'ncwellwise_cadmium_med') {
        layer = this.layers1.find(layer => layer.id === 'ncwellwise_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentradiovariable1 === 'ncwellwise_cadmium_mean') {
        layer = this.layers1.find(layer => layer.id === 'ncwellwise_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentradiovariable1 === 'ncwellwise_cadmium_prcast') {
        layer = this.layers1.find(layer => layer.id === 'ncwellwise_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentradiovariable1 === 'ncwellwise_lead_med') {
        layer = this.layers1.find(layer => layer.id === 'ncwellwise_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentradiovariable1 === 'ncwellwise_lead_mean') {
        layer = this.layers1.find(layer => layer.id === 'ncwellwise_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentradiovariable1 === 'ncwellwise_lead_prcast') {
        layer = this.layers1.find(layer => layer.id === 'ncwellwise_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentradiovariable1 === 'ncwellwise_manganese_med') {
        layer = this.layers1.find(layer => layer.id === 'ncwellwise_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentradiovariable1 === 'ncwellwise_manganese_mean') {
        layer = this.layers1.find(layer => layer.id === 'ncwellwise_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentradiovariable1 === 'ncwellwise_manganese_prcast') {
        layer = this.layers1.find(layer => layer.id === 'ncwellwise_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentradiovariable1 === 'cases') {
        layer = this.layers1.find(layer => layer.id === 'covid19_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentradiovariable1 === 'cases_per_10000_res') {
        layer = this.layers1.find(layer => layer.id === 'covid19_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentradiovariable1 === 'cases_per_100000_res') {
        layer = this.layers1.find(layer => layer.id === 'covid19_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentradiovariable1 === 'deaths') {
        layer = this.layers1.find(layer => layer.id === 'covid19_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentradiovariable1 === 'nolayer1') {
        layer = this.layers1.find(layer => layer.id === 'noLayer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      }

      if (layer != null) {
        layer.visible = true
      }
    },
    showMap2PanelRadioLayer: function () {
      let layer = this.layers2.find(layer => layer.visible)

      if (layer != null) {
        layer.visible = false
      }

      var i
      if (this.currentradiovariable2 === 'ncwellwise_arsenic_med') {
        layer = this.layers2.find(layer => layer.id === 'ncwellwise_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentradiovariable2 === 'ncwellwise_arsenic_mean') {
        layer = this.layers2.find(layer => layer.id === 'ncwellwise_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentradiovariable2 === 'ncwellwise_arsenic_prcast') {
        layer = this.layers2.find(layer => layer.id === 'ncwellwise_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentradiovariable2 === 'ncwellwise_cadmium_med') {
        layer = this.layers2.find(layer => layer.id === 'ncwellwise_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentradiovariable2 === 'ncwellwise_cadmium_mean') {
        layer = this.layers2.find(layer => layer.id === 'ncwellwise_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentradiovariable2 === 'ncwellwise_cadmium_prcast') {
        layer = this.layers2.find(layer => layer.id === 'ncwellwise_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentradiovariable2 === 'ncwellwise_lead_med') {
        layer = this.layers2.find(layer => layer.id === 'ncwellwise_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentradiovariable2 === 'ncwellwise_lead_mean') {
        layer = this.layers2.find(layer => layer.id === 'ncwellwise_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentradiovariable2 === 'ncwellwise_lead_prcast') {
        layer = this.layers2.find(layer => layer.id === 'ncwellwise_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentradiovariable2 === 'ncwellwise_manganese_med') {
        layer = this.layers2.find(layer => layer.id === 'ncwellwise_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentradiovariable2 === 'ncwellwise_manganese_mean') {
        layer = this.layers2.find(layer => layer.id === 'ncwellwise_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentradiovariable2 === 'ncwellwise_manganese_prcast') {
        layer = this.layers2.find(layer => layer.id === 'ncwellwise_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentradiovariable2 === 'cases') {
        layer = this.layers2.find(layer => layer.id === 'covid19_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentradiovariable2 === 'cases_per_10000_res') {
        layer = this.layers2.find(layer => layer.id === 'covid19_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentradiovariable2 === 'cases_per_100000_res') {
        layer = this.layers2.find(layer => layer.id === 'covid19_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentradiovariable2 === 'deaths') {
        layer = this.layers2.find(layer => layer.id === 'covid19_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentradiovariable2 === 'nolayer2') {
        layer = this.layers2.find(layer => layer.id === 'noLayer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      }

      if (layer != null) {
        layer.visible = true
      }
    },
    onMap1Click: function (event) {
      let pixel = event.pixel
      let features = this.$refs.map1.$map.getFeaturesAtPixel(pixel)
      let var1
      let var2

      if (features) {
        if (features.length > 1) {
          if ((this.map1pat1title.substring(0, 11) === 'ncwellwise_') && (this.map1pat2title.substring(0, 11) !== 'ncwellwise_')) {
            var1 = this.map1pat1title.substring(11)
            var2 = this.map1pat2title
          } else if ((this.map1pat1title.substring(0, 11) !== 'ncwellwise_') && (this.map1pat2title.substring(0, 11) !== 'ncwellwise_')) {
            var1 = this.map1pat1title
            var2 = this.map1pat2title
          } else if ((this.map1pat2title.substring(0, 11) === 'ncwellwise_') && (this.map1pat1title.substring(0, 11) !== 'ncwellwise_')) {
            var1 = this.map1pat1title
            var2 = this.map1pat2title.substring(11)
          }

          for (let i = 0; i < features.length; i++) {
            if (JSON.stringify(features[i].properties_).includes(var1) === true) {
              this.vtSelection = {}
              this.map1var1 = var1 + ': ' + features[i].properties_[var1].toString()
              let feature = features[i]
              let fid = feature.get(this.vtIdProp)
              this.vtSelection[fid] = feature
              this.$refs.layer1Style[i].refresh()
              // console.log(var1, this.$refs.layer1Style)
            }

            if (JSON.stringify(features[i].properties_).includes(var2) === true) {
              this.vtSelection = {}
              this.map1var2 = var2 + ': ' + features[i].properties_[var2].toString()
              let feature = features[i]
              let fid = feature.get(this.vtIdProp)
              this.vtSelection[fid] = feature
              this.$refs.layer1Style[i].refresh()
              // console.log(var2, this.$refs.layer1Style)
            }
          }
        } else {
          this.vtSelection = {}
          for (let i = 0; i < this.$refs.layer1Style.length; i++) {
            this.$refs.layer1Style[i].refresh()
          }
        }
      } else if (!features) {
        this.vtSelection = {}
        for (let i = 0; i < this.$refs.layer1Style.length; i++) {
          this.$refs.layer1Style[i].refresh()
        }
      }
    },
    onMap2Click: function (event) {
      let pixel = event.pixel
      let features = this.$refs.map2.$map.getFeaturesAtPixel(pixel)
      let var1
      let var2
      if (features) {
        if (features.length > 1) {
          if ((this.map2pat1title.substring(0, 11) === 'ncwellwise_') && (this.map2pat2title.substring(0, 11) !== 'ncwellwise_')) {
            var1 = this.map2pat1title.substring(11)
            var2 = this.map2pat2title
          } else if ((this.map2pat1title.substring(0, 11) !== 'ncwellwise_') && (this.map2pat2title.substring(0, 11) !== 'ncwellwise_')) {
            var1 = this.map2pat1title
            var2 = this.map2pat2title
          } else if ((this.map2pat2title.substring(0, 11) === 'ncwellwise_') && (this.map2pat1title.substring(0, 11) !== 'ncwellwise_')) {
            var1 = this.map2pat1title
            var2 = this.map2pat2title.substring(11)
          }

          for (let i = 0; i < features.length; i++) {
            if (JSON.stringify(features[i].properties_).includes(var1) === true) {
              this.vtSelection = {}
              this.map2var1 = var1 + ': ' + features[i].properties_[var1].toString()
              let feature = features[i]
              let fid = feature.get(this.vtIdProp)
              this.vtSelection[fid] = feature
              this.$refs.layer2Style[i].refresh()
            }

            if (JSON.stringify(features[i].properties_).includes(var2) === true) {
              this.vtSelection = {}
              this.map2var2 = var2 + ': ' + features[i].properties_[var2].toString()
              let feature = features[i]
              let fid = feature.get(this.vtIdProp)
              this.vtSelection[fid] = feature
              this.$refs.layer2Style[i].refresh()
            }
          }
        } else {
          this.vtSelection = {}
          for (let i = 0; i < this.$refs.layer2Style.length; i++) {
            this.$refs.layer2Style[i].refresh()
          }
        }
      } else if (!features) {
        this.vtSelection = {}
        for (let i = 0; i < this.$refs.layer2Style.length; i++) {
          this.$refs.layer2Style[i].refresh()
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
  .dualmap {
    margin: 0;
    padding: 1px;
    width: 50%;
    height: 100%;
  }
  /* .view {
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
  } */
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
  .pretsqu1 {
    height: 15px;
    width: 15px;
    background-color: rgba(207, 252, 242, 0.65);
    // background-color: var(--manganese-colors[1]);
    display: inline-block;
  }
  .pretsqu2 {
    height: 15px;
    width: 15px;
    background-color: rgba(140, 250, 224, 0.65);
    // background-color: var(--manganese-colors[2]);
    display: inline-block;
  }
  .pretsqu3 {
    height: 15px;
    width: 15px;
    background-color: rgba(46, 240, 162, 0.65);
    // background-color: var(--manganese-colors[3]);
    display: inline-block;
  }
  .pretsqu4 {
    height: 15px;
    width: 15px;
    background-color: rgba(3, 148, 90, 0.65);
    // background-color: var(--manganese-colors[4]);
    display: inline-block;
  }
  .q-input {
    height: 4.0em;
  }
  .q-select {
    height: 4.0em;
  }
  .vstrfill {
    border: solid 1px black;
    background: repeating-linear-gradient( 90deg, rgba(246, 250, 5, 1.0), rgba(246, 250, 5, 1.0) 5px, rgba(91, 95, 99, 0.0) 5px, rgba(91, 95, 99, 0.0) 10px);
    // background: repeating-linear-gradient( 90deg, var(--pattern1-colors[0]), var(--pattern1-colors[0]) 5px, rgba(91, 95, 99, 0.0) 5px, rgba(91, 95, 99, 0.0) 10px);
    height: 40px;
    width: 40px;
    display: inline-block;
  }
  .vstr11 {
    border: solid 1px black;
    background: repeating-linear-gradient( 90deg, rgba(2, 114, 250, 1.0), rgba(2, 114, 250, 1.0) 5px, rgba(0, 125, 125, 1.0) 5px, rgba(0, 125, 125, 1.0) 10px);
    height: 40px;
    width: 40px;
  }
  .vstr12 {
    border: solid 1px black;
    background: repeating-linear-gradient( 90deg, rgba(2, 114, 250, 1.0), rgba(2, 114, 250, 1.0) 5px, rgba(91, 240, 245, 1.0) 5px, rgba(91, 240, 245, 1.0) 10px);
    height: 40px;
    width: 40px;
  }
  .vstr13 {
    border: solid 1px black;
    background: repeating-linear-gradient( 90deg, rgba(2, 114, 250, 1.0), rgba(2, 114, 250, 1.0) 5px, rgba(250, 203, 92, 1.0) 5px, rgba(250, 203, 92, 1.0) 10px);
    height: 40px;
    width: 40px;
  }
  .vstr14 {
    border: solid 1px black;
    background: repeating-linear-gradient( 90deg, rgba(2, 114, 250, 1.0), rgba(2, 114, 250, 1.0) 5px, rgba(240, 129, 5, 1.0) 5px, rgba(240, 129, 5, 1.0) 10px);
    height: 40px;
    width: 40px;
  }
  .vstr21 {
    border: solid 1px black;
    background: repeating-linear-gradient( 90deg, rgba(150, 215, 250, 1.0), rgba(150, 215, 250, 1.0) 5px, rgba(0, 125, 125, 1.0) 5px, rgba(0, 125, 125, 1.0) 10px);
    height: 40px;
    width: 40px;
  }
  .vstr22 {
    border: solid 1px black;
    background: repeating-linear-gradient( 90deg, rgba(150, 215, 250, 1.0), rgba(150, 215, 250, 1.0) 5px, rgba(91, 240, 245, 1.0) 5px, rgba(91, 240, 245, 1.0) 10px);
    height: 40px;
    width: 40px;
  }
  .vstr23 {
    border: solid 1px black;
    background: repeating-linear-gradient( 90deg, rgba(150, 215, 250, 1.0), rgba(150, 215, 250, 1.0) 5px, rgba(250, 203, 92, 1.0) 5px, rgba(250, 203, 92, 1.0) 10px);
    height: 40px;
    width: 40px;
  }
  .vstr24 {
    border: solid 1px black;
    background: repeating-linear-gradient( 90deg, rgba(150, 215, 250, 1.0), rgba(150, 215, 250, 1.0) 5px, rgba(240, 129, 5, 1.0) 5px, rgba(240, 129, 5, 1.0) 10px);
    height: 40px;
    width: 40px;
  }
  .vstr31 {
    border: solid 1px black;
    background: repeating-linear-gradient( 90deg, rgba(250, 219, 202, 1.0), rgba(250, 219, 202, 1.0) 5px, rgba(0, 125, 125, 1.0) 5px, rgba(0, 125, 125, 1.0) 10px);
    height: 40px;
    width: 40px;
  }
  .vstr32 {
    border: solid 1px black;
    background: repeating-linear-gradient( 90deg, rgba(250, 219, 202, 1.0), rgba(250, 219, 202, 1.0) 5px, rgba(91, 240, 245, 1.0) 5px, rgba(91, 240, 245, 1.0) 10px);
    height: 40px;
    width: 40px;
  }
  .vstr33 {
    border: solid 1px black;
    background: repeating-linear-gradient( 90deg, rgba(250, 219, 202, 1.0), rgba(250, 219, 202, 1.0) 5px, rgba(250, 203, 92, 1.0) 5px, rgba(250, 203, 92, 1.0) 10px);
    height: 40px;
    width: 40px;
  }
  .vstr34 {
    border: solid 1px black;
    background: repeating-linear-gradient( 90deg, rgba(250, 219, 202, 1.0), rgba(250, 219, 202, 1.0) 5px, rgba(240, 129, 5, 1.0) 5px, rgba(240, 129, 5, 1.0) 10px);
    height: 40px;
    width: 40px;
  }
  .vstr41 {
    border: solid 1px black;
    background: repeating-linear-gradient( 90deg, rgba(153, 55, 2, 1.0), rgba(153, 55, 2, 1.0) 5px, rgba(0, 125, 125, 1.0) 5px, rgba(0, 125, 125, 1.0) 10px);
    height: 40px;
    width: 40px;
  }
  .vstr42 {
    border: solid 1px black;
    background: repeating-linear-gradient( 90deg, rgba(153, 55, 2, 1.0), rgba(153, 55, 2, 1.0) 5px, rgba(91, 240, 245, 1.0) 5px, rgba(91, 240, 245, 1.0) 10px);
    height: 40px;
    width: 40px;
  }
  .vstr43 {
    border: solid 1px black;
    background: repeating-linear-gradient( 90deg, rgba(153, 55, 2, 1.0), rgba(153, 55, 2, 1.0) 5px, rgba(250, 203, 92, 1.0) 5px, rgba(250, 203, 92, 1.0) 10px);
    height: 40px;
    width: 40px;
  }
  .vstr44 {
    border: solid 1px black;
    background: repeating-linear-gradient( 90deg, rgba(153, 55, 2, 1.0), rgba(153, 55, 2, 1.0) 5px, rgba(240, 129, 5, 1.0) 5px, rgba(240, 129, 5, 1.0) 10px);
    height: 40px;
    width: 40px;
  }
</style>
