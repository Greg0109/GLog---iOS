@interface GLog : NSObject
@property (nonatomic, retain) NSString *ip;
-(id)initWithIP:(NSString *)pcip;
-(void)sendLog:(NSString *)log;
@end