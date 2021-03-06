# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'AgentReviews.stars'
        db.add_column('api_agent_reviews', 'stars',
                      self.gf('django.db.models.fields.IntegerField')(default=5),
                      keep_default=False)


        # Changing field 'AgentReviews.review'
        db.alter_column('api_agent_reviews', 'review', self.gf('django.db.models.fields.TextField')(null=True))

    def backwards(self, orm):
        # Deleting field 'AgentReviews.stars'
        db.delete_column('api_agent_reviews', 'stars')


        # Changing field 'AgentReviews.review'
        db.alter_column('api_agent_reviews', 'review', self.gf('django.db.models.fields.TextField')(default=''))

    models = {
        'api.agentreviews': {
            'Meta': {'object_name': 'AgentReviews', 'db_table': "'api_agent_reviews'"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'agent_id': ('django.db.models.fields.IntegerField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'review': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'stars': ('django.db.models.fields.IntegerField', [], {'default': '5'})
        },
        'api.agents': {
            'Meta': {'object_name': 'Agents'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'online': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'picture_url': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'ratings': ('django.db.models.fields.IntegerField', [], {'default': '5'})
        },
        'api.akoshabusiness': {
            'Meta': {'object_name': 'AkoshaBusiness'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        'api.betadistrib': {
            'Meta': {'object_name': 'BetaDistrib', 'db_table': "'api_beta_distrib'"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'hex_code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'api.business': {
            'Meta': {'object_name': 'Business'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'android_recommended': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'category': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'country_code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'devicehelp_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'devicehelp_flag': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '250', 'null': 'True'}),
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'haptik_flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'ios_recommended': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'preview_text': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'unread': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'via_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'xmpp_handle': ('django.db.models.fields.EmailField', [], {'max_length': '250'})
        },
        'api.category': {
            'Meta': {'object_name': 'Category'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'api.chatcollections': {
            'Meta': {'object_name': 'ChatCollections'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'business_id': ('django.db.models.fields.IntegerField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'from_user': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'unread': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'api.chatmessaged': {
            'Meta': {'object_name': 'ChatMessaged'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'coll_id': ('django.db.models.fields.IntegerField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'direction': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'api.countriessupported': {
            'Meta': {'object_name': 'CountriesSupported', 'db_table': "'api_countries_supported'"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'callcode': ('django.db.models.fields.IntegerField', [], {}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'numberformat': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'api.faqs': {
            'Meta': {'object_name': 'Faqs'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'answer': ('django.db.models.fields.TextField', [], {}),
            'business': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['api.Business']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'question': ('django.db.models.fields.TextField', [], {}),
            'relevance': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'api.favourite': {
            'Meta': {'object_name': 'Favourite'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'business': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['api.Business']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['api.User']"})
        },
        'api.location': {
            'Meta': {'object_name': 'Location'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'api.smslog': {
            'Meta': {'object_name': 'SMSLog'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'country_code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'error': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'sent_successfully': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sms_sid': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'sms_type': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'api.user': {
            'Meta': {'object_name': 'User'},
            'activate_code': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'chat_notifications_allowed': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'coll_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'country_code': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'device_help_user': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'device_token': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '250', 'null': 'True'}),
            'fav_notifications_allowed': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'from_user': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'gender': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'unread': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'api.user2': {
            'Meta': {'object_name': 'User2', 'db_table': "'api_user_2'"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'coll_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'from_user': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'login_method': ('django.db.models.fields.IntegerField', [], {}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'unread': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user_name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'api.websitesignups': {
            'Meta': {'unique_together': "(('country_code', 'number'),)", 'object_name': 'WebsiteSignups', 'db_table': "'api_website_singups'"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'country_code': ('django.db.models.fields.CharField', [], {'default': "'91'", 'max_length': '250'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'downloaded': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'os_type': ('django.db.models.fields.IntegerField', [], {}),
            'text_sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['api']