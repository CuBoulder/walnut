<?php
/**
 * @file
 * Drupal site-specific configuration file.
 *
 * We include a pre and post local file so that we can set variables for the
 * main file and override config as needed.
 */
/**
 * Include a pre local settings file if it exists.
 */
global $conf;

// Google Data
{% if google_cse_csx -%}
$conf["google_cse_cx"] = "{{google_cse_csx}}";
{% else -%}
$conf["google_cse_cx"] = NULL;
{% endif %}
$conf['googleanalytics_account'] = 'UA-25752450-1';
{% if ( (google_tag_client_container_id) and (environment in ['local','dev','test']) ) %}
  $conf['google_tag_client_container_id'] = '{{ google_tag_client_container_id }}';
{% endif %}
// SMTP configuration, see also relevant hosting module install hook.
$conf["smtp_client_hostname"] = "{{smtp_client_hostname}}";
$conf["smtp_password"] = "{{smtp_password}}";

// simpleSAMLphp library location.
$conf['simplesamlphp_auth_installdir'] = $_ENV['HOME'] . '/code/private/simplesamlphp-1.17.6';

);